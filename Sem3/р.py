skr = {1: 'AEIOULNSTRАВЕИНОРСТ', 
       2: 'DGДКЛМПУ', 
        3: 'BCMPБГЁЬЯ',
         4: 'FHVWYЙЫ', 
          5: 'KЖЗХЦЧ', 
           8: 'JXШЭЮ', 
            10: 'QZФЩЪ'}
dr = 0
n = 'ноутбук'
m = n.upper()
for i in m:
       for x,y in skr.items():
              if i in y:
                      dr += x

print(dr)