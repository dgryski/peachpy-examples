import peachpy.x86_64

f = Argument(ptr())

with Function("add", (f,), uint64_t) as function:
    reg_f_base = GeneralPurposeRegister64()

    LOAD.ARGUMENT(reg_f_base, f)

    v = GeneralPurposeRegister64()

    # move and zero-extend 16-bit value at addr reg_f_base+2
    MOVZX(v, word[reg_f_base+2])
    ADD(v, [reg_f_base+8])

    RETURN(v)
