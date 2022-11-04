from random import choice, randint
import unittest


class Generator(object):
    
    @staticmethod
    def generate_binary_sequence(length_in_bits):
        bits=["0", "1"]
        sequence=""
        for i in range(0, length_in_bits):
            sequence=sequence+choice(bits)
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
        
        binary_sequence=Generator.convert_cidr_mask_to_binary(cidr_prefix_length)
        mask_with_dots=Generator.convert_binary_to_ip(binary_sequence)
        return mask_with_dots

    
    @staticmethod 
    def generate_class_a_ip_address():
        #Generamos 31 bits al azar y ponemos como primer bit el 0
        sequence=Generator.generate_binary_sequence(31)
        sequence="0"+sequence
        mask_bits=randint(6, 27)
        return (sequence, mask_bits)
    
    @staticmethod 
    def generate_class_b_ip_address():
        #Generamos 30 bits al azar y ponemos como primeros bits "10"
        sequence=Generator.generate_binary_sequence(30)
        sequence="10"+sequence
        mask_bits=randint(16, 27)
        return (sequence, mask_bits)

    @staticmethod 
    def generate_class_c_ip_address():
        #Generamos 29 bits al azar y ponemos como primeros bits "110"
        sequence=Generator.generate_binary_sequence(30)
        sequence="110"+sequence
        mask_bits=randint(24, 28)
        return (sequence, mask_bits)

class Tests(unittest.TestCase):
    def test_binary_sequence(self):
        length=24
        secuencia=Generator.generate_binary_sequence(length)
        self.assertEqual(length, len(secuencia))
    
    def test_bin_to_ip(self):
        length=32
        sequence=Generator.generate_binary_sequence(length)
        ip_address=Generator.convert_binary_to_ip(sequence)
        new_sequence=Generator.convert_ip_to_binary(ip_address, with_dots=False)
        self.assertEqual(sequence, new_sequence)
    def test_class_a_generation(self):
        (address, cidr_length)=Generator.generate_class_a_ip_address()
        address=Generator.convert_binary_to_ip(address)
        cadena="{0}/{1}".format(address, cidr_length)
        #print(cadena)
    def test_class_b_generation(self):
        (direccion_clase_b, bits_red)=Generator.generate_class_b_ip_address()
        direccion_clase_b=Generator.convert_binary_to_ip(direccion_clase_b)
        cadena="{0}/{1}".format(direccion_clase_b, bits_red)
        #print(cadena)
    def test_class_c_generation(self):
        (direccion_clase_c, bits_red)=Generator.generate_class_c_ip_address()
        direccion_clase_c=Generator.convert_binary_to_ip(direccion_clase_c)
        cadena="{0}/{1}".format(direccion_clase_c, bits_red)
        #print(cadena)
    def test_convertir_cidr_a_binario(self):
        sequence="1"*32
        bits=32
        converted_sequence=Generator.convert_cidr_mask_to_binary(bits)
        self.assertEqual(sequence, converted_sequence)

        sequence="1"*30+"00"
        bits=30
        converted_sequence=Generator.convert_cidr_mask_to_binary(bits)
        self.assertEqual(sequence, converted_sequence)

        sequence="1"*20+"0"*12
        bits=20
        converted_sequence=Generator.convert_cidr_mask_to_binary(bits)
        
        self.assertEqual(sequence, converted_sequence)
        
    def test_convert_mask_to_decimal(self):
        mascara_calculada=Generator.convert_cidr_mask_to_decimal(32)
        mascara_esperada="255.255.255.255"
        self.assertEqual(mascara_calculada, mascara_esperada)

        mascara_calculada=Generator.convert_cidr_mask_to_decimal(24)
        mascara_esperada="255.255.255.0"
        self.assertEqual(mascara_calculada, mascara_esperada)

        mascara_calculada=Generator.convert_cidr_mask_to_decimal(16)
        mascara_esperada="255.255.0.0"
        self.assertEqual(mascara_calculada, mascara_esperada)

        mascara_calculada=Generator.convert_cidr_mask_to_decimal(18)
        mascara_esperada="255.255.192.0"
        self.assertEqual(mascara_calculada, mascara_esperada)

        
        
        

if __name__=="__main__":
    unittest.main()
from random import choice, randint
import unittest


