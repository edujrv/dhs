#
BUILD = ../build 
LDIR = ../libs
DEPS = main.c $(LDIR)/sumar.c $(LDIR)/sumar.h 
CFLAGS = -Wall

all : pc

main.o: main.c
		gcc -c -Wall main.c

sumar.o: sumar.c
		gcc -c -Wall sumar.c
		
exec: main.o sumar.o
		gcc main.o sumar.o

pc : $(DEPS)
	mkdir -p $(BUILD)
	gcc $(CFLAGS) -o ../build/pc -I$(LDIR) main.c $(LDIR)/sumar.c
#   no se porq no me toma el -o $(BUILD)/pc  

clean: 
	rm -rf $(BUILD)


