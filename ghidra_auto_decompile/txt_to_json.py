import json, sys, collections, os

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("[!] ERROR: no argument passed")
        sys.exit()
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()
    file_name = sys.argv[1].replace('txt', 'json')
    
    lines = [line.strip().replace("'","\"") for line in lines]
    dict_collection = [json.loads(line) for line in lines]
    super_dict = collections.defaultdict(list)
    for d in dict_collection:
        for k, v in d.items():
            super_dict[k].append(v)
    
    with open(file_name,'w') as f:
        json.dump(super_dict, f, ensure_ascii=False, indent=4)
        
    # remove txt file
    os.remove(sys.argv[1])
    print(f"[*] changed {sys.argv[1]} to {file_name}")
    
