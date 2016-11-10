import peachpy.x86_64

s_data = Argument(ptr())
s_len = Argument(size_t)
s_cap = Argument(size_t)

with Function("add", (s_data,s_len,s_cap), uint64_t) as function:
    reg_s_data = GeneralPurposeRegister64()
    reg_s_len = GeneralPurposeRegister64()

    LOAD.ARGUMENT(reg_s_data, s_data)
    LOAD.ARGUMENT(reg_s_len, s_len)

    total = GeneralPurposeRegister64()
    XOR(total, total)

    with Loop() as loop:
        ADD(total, [reg_s_data])
        ADD(reg_s_data, 8)
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
