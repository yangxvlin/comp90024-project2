import subprocess
import os
import json

def main():
    files = os.listdir("./processed")

    if os.path.isfile("concate.jsonl"):
        return

    pd = [[],[],[]]

    for fn in files:
        source = os.path.join("./processed", fn)
        with open(source, "r") as f:
            d = json.load(f)
            pd[2].append(d["geo_code"])
            pd[0].append(d['polarity'])
            pd[1].append(d["subjectivity"])
            
    with open("test.csv", "w") as f:
        f.writelines("polarity,subjectivity,geo\n")
        
        for i in range(len(pd[0])):
            for j in range(len(pd)):
                f.writelines(str(pd[j][i]))
                if j < len(pd) -1:
                    f.writelines(",")
            f.writelines("\n")
    
if __name__ == "__main__":
    main()
