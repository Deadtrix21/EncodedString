from EncodedStrings import Encoding
mod = Encoding()
aa = mod.SyncModule.BasicEncode.Encode.hex("Hello World")
bb = mod.SyncModule.BasicEncode.Decode.hex(aa)

print(aa)
print(bb)