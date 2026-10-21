# paths = ["docs/report.PDF", "notes.txt", "docs/img/logo.png", "Makefile"]
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
# print(f(paths))

# for i in paths:
#     r = {}
#     for i in paths:
#         d = i.split('.')
#         if len(d) != 2:
#             r[""] += 1
#         else:
#             r.get(f"{d[1]}")
#             r[f"{d[1]}"] += 1  


       