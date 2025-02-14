import time
print("Hello user, may I know your name?")

name = input("Enter your name: ")
time.sleep(1)
print("Hello," + name, "This is an engineering dictionary.")
time.sleep(1)
print("I Have A - U terms. this is what i have in store: ")

time.sleep(1)
print("A (ABACUS, ACTUATOR,'ANALYTICAL ENGINE)")

print("B (BANDSAW)")

print("C (CARRIAGE)")

print("D (DIE)")

print("E (ELECTRIC MOTOR)")

print("F (FABRICATION, FIRST GENERATION)")

print("G (GAUGE)")

print("H (HACKSAW, HARD DISK DRIVE)")

print ("I (IGNITORS)")

print("J (JIG SAW STEEL)")

print("K (KNURL)")

print("L (LAMINATION, LEIBNIZ WHEEL)")

print("M (MACHINE DRAWING, MARK I)")

print("N (NAPIER'S BONES, NEEDLES)")

print("O (ORE)")

print("P (PASCALINE)")

print("Q (QUENCHING)")

print("R (RANDOM ACCESS MEMORY)")

print("S (SECOND GENERATION)")

print("T (TABULATING MACHINE, TAPE MEASURE, THIRD GENERATION)")

print("U (UNDERWRAP)")

time.sleep(1)


Data = { 
	"ACTUATOR": "A device for converting hydraulic energy into mechanical energy, examples are a motor or a cylinder.",
	"BANDSAW": "A power saw, the blade of which is a continous, narrow, steel band having teeth on one edge and passing over two large pulley wheels.",
	"CARRIAGE": "A belt mounted on wheels that is used to move materials from one storage bin to another.",
	"DIE": "A metal block used in forming materials by casting, molding, stamping, threading, or extruding.",
	"ELECTRIC MOTOR": "An electromechanical device that converts electrical power into rotary motion, measured in horsepower. ",
	"ABACUS": "The first computer, invented 4000 years ago, Chinese Invented this",
	"NAPIER'S BONES" : "Multiply and divide, uses 9 different ivory bones, uses decimal points",
	"PASCALINE": "Adding machine, invented between 1642 and 1644, first mechanical and automatic calculator",
	"TABULATING MACHINE": "invented in the year 1890, A mechanical Tumbulator based om punch cards",
	"ANALYTICAL ENGINE": "invented in the year 1830, by Charles Babbage, was a mechanical computer",
	"LEIBNIZ WHEEL": "invented in the year 1673, basically a digital machanical calculator, made of fluted drums",
	"MARK I": "invented in the year 1937, invented by Howard Aiken, with the partner ship between IBM and Harvard",
	"FIRST GENERATION": "Period of the year 1940-1956, slow, huge and expensive, dependent on the batch operating aystems." ,
	"SECOND GENERATION" : "Period of the year 1957-1963, trasistors are used, compact and consume less power",
	"THIRD GENERATION" : "Period of yhe year 1964 to 1971, integrated circuits were used, consist of many transistors to increase power",
	"FABRICATION": "The joining, usually by welding, of two or more parts to produce a finished assembly. The components of the assembly may be a combination of cast and wrought materials.",
"GAUGE" : "The thickness of sheet steel. Better quality steel has a consistent gauge to prevent weak spots or deformation.",
"HACKSAW" : "A metal blade of hardened steel having small, close teeth on one edge. It is held under tension in a U shaped frame.",
"IGNITORS" : "Devices which employ a high energy electrical spark to ignite the pilot gas flame.",
"JIG SAW STEEL" : "Hardened, tempered and bright polished with round edges. Carbon content .85. Ranges of sizes .039 to 393 in width and .016 to .039 in thickness.",
"KNURL" : "A decorative gripping surface of straight line or diagonal design made by uniformly serrated rolls called knurls.",
"LAMINATION" : "An abnormal structure resulting in a separation or weakness aligned generally parallel to the worked surface of the metal.",
"MACHINE DRAWING" : "An engineering drawing which depicts the final size and shape of the part for its end use.",
"RANDOM ACCESS MEMORY" : "Also know as RAM, it is an electronic device that is much faster than HDD but has volatile memory.",
"HARD DISK DRIVE" : "Also know as HDD, it is an electromechanical device, slower than RAM but can store files permanently.",
"NEEDLES" : "Elongated acicular crystals, tapering at each end to a fine point, as martensite.",
"ORE" : "An iron bearing material used primarily in the blast furnace.",
"QUENCHING" : "Rapid cooling of hardening; normally achieved by immersion of the object to be hardened in water, oil, or solutions of salt or organic compounds in water.",
"TAPE MEASURE" : "Tool used to measure the width of the coil.",
"UNDERWRAP" : "The direction which coils are being wrapped or unwrapped. If coil is underwrapping the reel is turning and the steel is fed from the bottom."
}

a = input("What do you want to know? : ")
print("Searching for the definition of," +(a), ".........")
time.sleep(0.5)
print("......Please wait......")
time.sleep(1)
print("............ Definition found!")
time.sleep(1)
print(Data[ a ])

time.sleep(1)
print("I hope my dictionary helped! Thank you!")
