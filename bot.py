import discord
from discord.ext import commands
import io
import os
from PIL import  Image
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix="o!", intents=intents, help_command = None)

@bot.event
async def on_ready():
    print(f"Bot online: {bot.user}")
    print(f"Logged in as {bot.user}")
    channel = bot.get_channel(1469204961400459288)
    await channel.send("Bot is on now")
@bot.command()
async def help(ctx):
    await ctx.send("```=====2k14 bot=====```")
    await ctx.send("```1) o!p2h : how to use => o!p2h [weight] [ higth] [threshold] [picture] => use for convert the picture to bitmap and hex```")
    await ctx.send("```2) o!hex2token : how to use => o!hex2token [hex1] [hex2] [...] => use for convert hex to token```")

@bot.command()
async def ping(ctx):
    help = "```check bot on or off```"
    usage = "```o!ping```"
    await ctx.send("pong 🏓")
@bot.command()
async def hello(ctx):
    await ctx.send("hello👍")
@bot.command()
async def check(ctx):
    await ctx.send("```ver0.beta. Made by @unkorn. Supporter : @jsaidoru```")
@bot.command()
async def pingUser(ctx, member: discord.Member, *, text):
    await ctx.send(f"{member.mention} {text}")
@bot.command()
async def spam(ctx, number_input: int, *, text):
    for i in range(number_input):
        await ctx.send(f"{text}")
    if number_input > 10:
        await ctx.send("spam it lai deee🥀")
        return
@bot.command()
@commands.is_owner()
async def shutdown(ctx):
    await ctx.send("bot is sleeping now...")
    await bot.close()


#==================
#upgrade h2t
# dict >> list
#=================
singlebyte_table =[
    "@", "<01>", "@", "@", "@", "@", "@", "@", "@", "@", "@", "@", "@", "@", "@", "@",
    "@", "@", "@", "@", "@", "@", "@", "@", "@", "▯", "@", "@", "@", "@", "@", "@",
    "𝒊", "𝒆", "𝜋", ":", "$", "?", "@", "@", "@", "@", "@", "@", ",", "x10", ".", "@",
    "0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "𝗔", "𝗕", "𝗖", "𝗗", "𝗘", "𝗙",
    "M", "Ans", "A", "B", "C", "D", "E", "F", "𝒙", "𝒚", "PreAns", "𝒛", "𝜃", "@", "@", "@",
    "∑(", "∫(", "d/d𝒙(", "∏(", "@", "@", "@", "@", "Min(", "Max(", "Mean(", "Sum(", "@", "@", "@", "@",
    "(", "P(", "Q(", "R(", "Not(", "Neg(", "Conjg(", "Arg(", "Abs(", "Rnd(", "Det(", "Trn(", "sinh(", "cosh(", "tanh(", "sinh⁻¹(",
    "cosh⁻¹(", "tanh⁻¹(", "𝒆^(", "10^(", "√(", "ln(", "³√(", "sin(", "cos(", "tan(", "sin⁻¹(", "cos⁻¹(", "tan⁻¹(", "log(", "Pol(", "Rec(",
    "@", "@", "@", "Int(", "Intg(", "Ref(", "Rref(", "RanInt#(", "GCD(", "LCM(", "RndFix(", "@", "@", "@", "@", "ReP(",
    "ImP(", "Identity(", "UnitV(", "Angle(", "@", "@", "@", "@", "@", "@", "@", "@", "@", "@", "@", "@",
    "or", "xor", "xnor", "and", "@", "=", "+", "-", "×", "÷", "÷R", "⋅", "∠", "𝗣", "𝗖", "@",
    "@", "@", "@", "@", "@", "@", "@", "@", "x̂", "ŷ", "x̂₁", "x̂₂", "@", "@", "@", "@",
    "−", "b", "o", "d", "h", "@", "@", "@", "⌟", "^(", "ˣ√(", "@", "@", "@", "@", "@",
    ")", "▸t", "▸a+b𝒊", "▸r∠𝜃", "⁻¹", "²", "³", "%", "!", "°", "ʳ", "ᵍ", "▫", "𝐄", "𝐏", "𝐓",
    "𝐆", "𝐌", "𝐤", "𝐦", "𝝁", "𝐧", "𝐩", "𝐟", "@", "▸Simp", "@", "@", "@", "@", "@"
]
multibyte_table = {
    "FA00" : "@", "FA01" : "ch▸yd", "FA02" : "yd▸ch", "FA03" : "ch▸mile", "FA04" : "mile▸ch", "FA05" : "mil▸in", "FA06" : "in▸mil", "FA07" : "fath▸in", "FA08" : "in▸fath",
    "FA09" : "fath▸ft", "FA0A" : "ft▸fath", "FA0B" : "fath▸yd", "FA0C" : "yd▸fath", "FA0D" : "ha▸a", "FA0E" : "a▸ha", "FA0F" : "mile²▸acre", "FA10" : "acre▸mile²",
    "F011" : "bu▸gal(UK)", "FA12" : "gal(UK)▸bu", "FA13" : "lb▸oz", "FA14" : "oz▸lb",
}
def translate_hex(hex_string: str):
    parts = hex_string.upper().strip().split()
    result = []

    i = 0
    while i < len(parts):

        # thử 2 byte trước
        if i + 1 < len(parts):
            two = parts[i] + " " + parts[i+1]
            if two in multibyte_table:
                result.append(multibyte_table[two])
                i += 2
                continue

        # fallback 1 byte
        one = parts[i]
        if one in singlebyte_table:
            result.append(singlebyte_table[one])
        else:
            result.append(f"<{one}>")

        i += 1

    return " ".join(result)
#command
@bot.command()
async def hex2token(ctx, *args):
    hex_input = " ".join(args)
    output = translate_hex(hex_input)
    await ctx.send(output)
#=P2H, O!P2H WIGTH HEIGHT PICTURE
THRESHOLD = 128

@bot.command()
async def p2h(ctx, width: int, height: int):
    # Validate
    if width <= 0 or width > 192:
        await ctx.send("❌ width phải > 0 và <= 192")
        return

    if height <= 0 or height > 63:
        await ctx.send("❌ height phải > 0 và <= 63")
        return

    if not ctx.message.attachments:
        await ctx.send("❌ Bạn cần gửi kèm ảnh.")
        return

    attachment = ctx.message.attachments[0]

    if not attachment.filename.lower().endswith((".png", ".jpg", ".jpeg", ".tiff", ".pdf", ".bmp", ".webp")):
        await ctx.send("❌ Chỉ hỗ trợ PNG / JPG / TIFF / PDF / BMP / WEBP")
        return

    try:
        # Đọc ảnh từ Discord (không cần lưu file)
        image_bytes = await attachment.read()
        img = Image.open(io.BytesIO(image_bytes)).convert("L")

        # Resize
        img = img.resize((width, height), Image.NEAREST)
        px = img.load()

        bits = []

        for y in range(height):
            for x in range(width):
                bit = 1 if px[x, y] < THRESHOLD else 0
                bits.append(bit)
                px[x, y] = 0 if bit == 1 else 255  # tạo preview trắng đen

        while len(bits) % 8 != 0:
            bits.append(0)

        hex_data = []

        for i in range(0, len(bits), 8):
            byte = 0
            for b in bits[i:i+8]:
                byte = (byte << 1) | b
            hex_data.append(f"{byte:02X}")

        # ===== TẠO FILE TXT =====
        hex_text = (
            f"Width {width}\n"
            f"Height {height}\n"
            f"HEX:\n"
            + " ".join(hex_data)
        )

        txt_file = discord.File(
            io.BytesIO(hex_text.encode()),
            filename="output.txt"
        )

        # ===== TẠO PREVIEW IMAGE =====
        img_bytes = io.BytesIO()
        img.save(img_bytes, format="PNG")
        img_bytes.seek(0)

        preview_file = discord.File(img_bytes, filename="preview.png")

        await ctx.send(
            content="✅ Convert thành công!",
            files=[preview_file, txt_file]
        )

    except Exception as e:
        await ctx.send(f"⚠️ Lỗi: {e}")

#run code
bot.run(TOKEN)
#allalal
