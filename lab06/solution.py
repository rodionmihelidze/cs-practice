from math import floor

def count_by_extension(paths):
    r = {}
    for i in paths:
      n = i.split("/")[-1]
      d = n.rsplit('.', 1)
      if len(d) != 2:
        r[""] = r.get("", 0) + 1
      else:
        p = d[1].lower()
        r[p] = r.get(p, 0) + 1
    return r

for i in paths:
    n = i.split("/")[-1]
    d = n.rsplit(".", 1)
    print(d)
def deepest_path(paths):
    b = []
    m = []
    s = ''
    for i in paths:
      m.append(i.split("/"))
    for j in range(len(m) - 1):
      if len(m[j]) >= len(m[j + 1]):
        b.append(j)
      else:
        b.append(j + 1)
    if len(b) > 0:
      s += f'{paths[max(b)]}'
    else:
      s = ''
    return s

def human_size(x):
  bites = ["Б", "КБ", "МБ", "ГБ", "ТБ"]
  size = x
  i = 0
  while size >= 1024 and i < 4:
    size = size / 1024
    i += 1
  if i == 0:
    return f"{size:.0f} {bites[i]}"
  return f"{size:.1f} {bites[i]}"


   
  
