Project Name: Certificate Generator
By: Suchismita Das

Description:
This Python project automatically generates course participation certificates. It uses a template image and adds the student’s name, course, and date from a text file.

How to Use:

1. Install Python

2. Install Pillow:

pip install pillow

3. Put your details in names_temp.txt like this:

Aditi Sen, Application Development Course, 22-07-25
Ravi Kumar, Data Science Bootcamp, 23-07-25

4. Run the script:

python certificate_generator.py

Certificates will be saved in the generated_certs folder.

Files Included:

generate_certificates.py – the main Python script

template_cert.jpg – background certificate

font_temp.ttf – the font used

names_temp.txt – the list of names

generated_certs/ – folder with final certificates