// Generated by PeachPy 0.2.0 from add.py


// func add(f1 uint64, f2 uint16) uint64
TEXT ·add(SB),4,$0-24
	MOVQ f1+0(FP), AX
	MOVWQZX f2+8(FP), BX
	ADDQ BX, AX
	MOVQ AX, ret+16(FP)
	RET
