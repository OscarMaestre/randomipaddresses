import unittest
from random import choice, randint
import ipaddress

class Generator(object):
    def get_binary_random_ip_address(self):
        choices=[   Helper.generate_class_a_ip_address, 
                    Helper.generate_class_b_ip_address, 
                    Helper.generate_class_c_ip_address, ]
        (address, prefix_length)=choice(choices)()
        return (address, prefix_length)

    def get_random_network_ip_address(self):
        (address, prefix_length)=self.get_binary_random_ip_address()
        decimal_address=Helper.convert_binary_to_ip(address)
        ip_template="{0}/{1}".format(decimal_address, prefix_length)
        network_address=ipaddress.ip_network(ip_template)
        return network_address

    
        
        
class Helper(object):
    
    @staticmethod
    def generate_binary_sequence(length_in_bits, as_string=True):
        bits=["0", "1"]
        sequence=[]
        for i in range(0, length_in_bits):
            sequence.append(choice(bits))
        if as_string:
            return "".join(sequence)
        else:
            return sequence
    @staticmethod
    def convert_ip_to_binary(ip, with_dots=True):
        if with_dots:
            separator="."
        else:
            separator=""

        ip_address= separator.join([bin(int(x)+256)[3:] for x in ip.split('.')])
        return ip_address
    @staticmethod
    def convert_binary_to_ip(binary_sequence):
        chunks = [binary_sequence[0:8], binary_sequence[8:16], binary_sequence[16:24], binary_sequence[24:32]]
        
        sequence=[]
    
        for chunk in chunks:
            sequence.append(str(int(chunk, 2)))
        ip=".".join(sequence)
        return ip

    @staticmethod
    def convert_cidr_mask_to_binary(cidr_prefix_length):
        mask=("1"*cidr_prefix_length)+("0"*(32-cidr_prefix_length))
        return mask

    @staticmethod
    def convert_cidr_mask_to_decimal(cidr_prefix_length):
        
        binary_sequence=Helper.convert_cidr_mask_to_binary(cidr_prefix_length)
        mask_with_dots=Helper.convert_binary_to_ip(binary_sequence)
        return mask_with_dots

    
    @staticmethod
    def generate_network_address(prefix, min_bits, max_bits):
        mask_bits=randint(min_bits, max_bits)
        sequence=Helper.generate_binary_sequence(32, as_string=False)
        for pos, bit in enumerate(prefix):
            sequence[pos]=bit
        for pos in range(mask_bits, 32):
            sequence[pos]="0"
        bit_sequence="".join(sequence)
        # print("==================")
        # print("Bit sequence:"+bit_sequence)
        # print("Prefix:      "+Helper.convert_cidr_mask_to_binary(mask_bits))
        # print("==================")
        return (bit_sequence, mask_bits)

    @staticmethod 
    def generate_class_a_ip_address():
        return Helper.generate_network_address("0", 6,30)
    
    @staticmethod 
    def generate_class_b_ip_address():
        return Helper.generate_network_address("10", 16,30)

    @staticmethod 
    def generate_class_c_ip_address():
        return Helper.generate_network_address("110", 24,30)

class Tests(unittest.TestCase):
    def test_binary_sequence(self):
        length=24
        secuencia=Helper.generate_binary_sequence(length)
        self.assertEqual(length, len(secuencia))
    
    def test_bin_to_ip(self):
        length=32
        sequence=Helper.generate_binary_sequence(length)
        ip_address=Helper.convert_binary_to_ip(sequence)
        new_sequence=Helper.convert_ip_to_binary(ip_address, with_dots=False)
        self.assertEqual(sequence, new_sequence)
    def test_class_a_generation(self):
        (address, cidr_length)=Helper.generate_class_a_ip_address()
        address=Helper.convert_binary_to_ip(address)
        cadena="{0}/{1}".format(address, cidr_length)
        #print(cadena)
    def test_class_b_generation(self):
        (direccion_clase_b, bits_red)=Helper.generate_class_b_ip_address()
        direccion_clase_b=Helper.convert_binary_to_ip(direccion_clase_b)
        cadena="{0}/{1}".format(direccion_clase_b, bits_red)
        #print(cadena)
    def test_class_c_generation(self):
        (direccion_clase_c, bits_red)=Helper.generate_class_c_ip_address()
        direccion_clase_c=Helper.convert_binary_to_ip(direccion_clase_c)
        cadena="{0}/{1}".format(direccion_clase_c, bits_red)
        #print(cadena)
    def test_convertir_cidr_a_binario(self):
        sequence="1"*32
        bits=32
        converted_sequence=Helper.convert_cidr_mask_to_binary(bits)
        self.assertEqual(sequence, converted_sequence)

        sequence="1"*30+"00"
        bits=30
        converted_sequence=Helper.convert_cidr_mask_to_binary(bits)
        self.assertEqual(sequence, converted_sequence)

        sequence="1"*20+"0"*12
        bits=20
        converted_sequence=Helper.convert_cidr_mask_to_binary(bits)
        
        self.assertEqual(sequence, converted_sequence)
        
    def test_convert_mask_to_decimal(self):
        mascara_calculada=Helper.convert_cidr_mask_to_decimal(32)
        mascara_esperada="255.255.255.255"
        self.assertEqual(mascara_calculada, mascara_esperada)

        mascara_calculada=Helper.convert_cidr_mask_to_decimal(24)
        mascara_esperada="255.255.255.0"
        self.assertEqual(mascara_calculada, mascara_esperada)

        mascara_calculada=Helper.convert_cidr_mask_to_decimal(16)
        mascara_esperada="255.255.0.0"
        self.assertEqual(mascara_calculada, mascara_esperada)

        mascara_calculada=Helper.convert_cidr_mask_to_decimal(18)
        mascara_esperada="255.255.192.0"
        self.assertEqual(mascara_calculada, mascara_esperada)

    def test_generator_1(self):
        g=Generator()        
        (address, prefix_length)=g.get_binary_random_ip_address()
        #print( (address, prefix_length))

    def test_random_network(self):
        g=Generator()
        network_address=g.get_random_network_ip_address()
        #print(network_address)


if __name__=="__main__":
    unittest.main()
    # Helper.generate_class_a_ip_address()
    # Helper.generate_class_b_ip_address()
    # Helper.generate_class_c_ip_address()
