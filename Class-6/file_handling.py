# 📦 File Handling kya hoti hai?
# File handling ka matlab hota hai:

# Python ke zariye kisi file ko create, read, write ya update karna.

# Hum computer ko instructions dete hain:

# Kis file ko kholna hai?

# Usme kya likhna ya parhna hai?

# Aur baad mein usay band karna hai.

# 📖 Daily Life Example
# Socho tum ek diary likhti ho:

# Diary kholti ho → open("diary.txt")

# Kuch likhti ho → write("Aaj ka din acha tha")

# Padhti ho → read()

# Band karti ho → close()


# 1. File banana aur usme likhna (Write Mode - w)

file = open("note.txt", "w")
file.write("How are you?")
file.close()
# 📝 Agar note.txt file exist nahi karti to Python khud bana dega.


# 2. File read karna (Read Mode - r)

file = open("note.txt", "r")
content = file.read()
print(content)
file.close()


# 3. File ko line by line parhna

with open("note.txt", "r") as file:
    for line in file:
        print(line)


# 4. Read + Write dono karna (Mode: r+)

with open("note.txt", "r+") as f:
    f.write(" - Added by Mahab.")
    f.seek(0)  # Cursor ko start par le jaane ke liye
    print(f.read())


# 🔐 with ka use kyu karein?
# with likhne se file automatic close ho jaati hai, tumhein close() likhne ki zarurat nahi padti.

with open("note.txt", "r") as file:
    print(file.read())



