paths = ["docs/report.PDF", "notes.txt", "docs/img/logo.png", "Makefile"]
def count_by_extension(paths):
    r = {}
    for i in paths:
        d = i.split('.')
        if len(d) != 2:
          r[""] = 0
          r[""] += 1
        else:
           r[f"{d[1]}"] = 0
           r[f"{d[1]}"] += 1
    return r


def desert_path(paths):
    b = []
    m = []
    for i in paths:
      m.append(i.split("/"))
    for j in range(len(m) - 1):
      if len(m[j]) > len(m[j + 1]):
        b.append(j)
      else:
        b.append(j + 1)
    return paths[max(b)]
print(desert_path(paths))


  
