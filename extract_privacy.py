import os
import shutil
from langdetect import detect

old_privacy_dir = "./selen_text/"
new_privacy_dir = "./final_text/"
old_privacy_list = os.listdir(old_privacy_dir)


# # replace the md file to txt
# def extract_privacy(old_privacy_dir, new_privacy_dir, old_privacy_list):
#     scrawed_privacy_list = []
#     for file in old_privacy_list:
#         old_privacy = old_privacy_dir+file
#         with open(old_privacy, "r", encoding="utf-8") as f:
#             content = f.read()
#             if len(content) > 0 and detect(content) == "en":
#                 shutil.copyfile(old_privacy, new_privacy_dir+file.replace(".md", ".txt"))
#         scrawed_privacy_list.append(file.replace(".md", ""))
#
#     orgin_urls = set()
#     with open("./set/privacy_policy_url.txt", "r", encoding="utf-8") as rfile:
#         orgin_urls = set([f.strip() for f in rfile])
#
#     uncrawl = [url+'\n' for url in orgin_urls if url.split('/')[2].split(':')[0] not in scrawed_privacy_list]
#     with open("./set/uncrawl.txt", "w", encoding="utf-8") as f:
#         f.writelines(uncrawl)


privacy_list = os.listdir(new_privacy_dir)
#remove unEnglish
for file in privacy_list:
    old_privacy = new_privacy_dir+file
    with open(str(old_privacy), "r", encoding="utf-8", errors='ignore') as f:
        content = f.read()
        if len(content) == 0 or detect(content) != "en":
            try:
                os.remove(old_privacy)
            except:
                print(old_privacy)




