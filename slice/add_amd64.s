// Generated by PeachPy 0.2.0 from add.py


// func add(s_data uintptr, s_len uint, s_cap uint) uint64
TEXT ·add(SB),4,$0-32
	MOVQ s_data+0(FP), AX
	MOVQ s_len+8(FP), BX
	XORQ CX, CX
loop_begin:
		ADDQ 0(AX), CX
		ADDQ $8, AX
		SUBQ $1, BX
		JNE loop_begin
	MOVQ CX, ret+24(FP)
	RET