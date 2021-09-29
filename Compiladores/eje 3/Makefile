BUILD = ../build 
LDIR = ../libs
DEPS = main.c $(LDIR)/arrays_utils.c $(LDIR)/arrays_utils.h
CFLAGS =- Wall

all : pc

main.o: main.c
		gcc -c -Wall main.c

sumar.o: sumar.c
		gcc -c -Wall sumar.c

exec: main.o sumar.o
		gcc main.o sumar.o

pc : $(DEPS)
	mkdir -p $(BUILD)
	gcc $(CFLAGS) -o $(BUILD)/pc -I$(LDIR) main.c $(LDIR)/arrays_utils.c

clean: 
	rm -rf $(BUILD)