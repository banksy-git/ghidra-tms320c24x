buildExtension: sleigh
	gradle buildExtension

clean:
	gradle clean

sleigh:
	/opt/ghidra_11.4.1_PUBLIC/support/sleigh -a data/languages

asm:
	~/src/libasm/cli/asm -C TMS320C5X test.asm -o test.hex
