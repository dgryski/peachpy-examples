import peachpy.x86_64

s_base = Argument(ptr())
s_len = Argument(size_t)
s_cap = Argument(size_t)

with Function("add", (s_base,s_len,s_cap), uint64_t) as function:
    reg_s_base = GeneralPurposeRegister64()
    reg_s_len = GeneralPurposeRegister64()

    LOAD.ARGUMENT(reg_s_base, s_base)
    LOAD.ARGUMENT(reg_s_len, s_len)

    total = GeneralPurposeRegister64()
    XOR(total, total)

    with Loop() as loop:
        ADD(total, [reg_s_base])
        ADD(reg_s_base, 8)
        SUB(reg_s_len, 1)
        JNZ(loop.begin)

    RETURN(total)

if __name__ == "__main__":
    import ctypes
    add_asm = function.finalize(abi.detect()).encode().load()
    inp = [10,500,2000,50000]
    arr = (ctypes.c_ulonglong * len(inp))(*inp)
    g = add_asm(arr,len(arr),len(arr))
    assert(g == 52510)
