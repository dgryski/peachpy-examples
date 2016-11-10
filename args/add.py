import peachpy.x86_64

f1 = Argument(uint64_t)
f2 = Argument(uint16_t)

with Function("add", (f1, f2), uint64_t) as function:
    reg_f1 = GeneralPurposeRegister64()
    reg_f2 = GeneralPurposeRegister64()

    LOAD.ARGUMENT(reg_f1, f1)
    LOAD.ARGUMENT(reg_f2, f2)

    ADD(reg_f1, reg_f2)

    RETURN(reg_f1)
