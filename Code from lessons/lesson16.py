
def football():
    #keys: carries, rushyds, rushtds
    jax = {}
    jax['carries'] = 100
    jax['rushyds'] = 1500
    jax['rushtds'] = 10
    caleb = {'carries': 101, 'rushyds': 1501, 'rushtds': 11}
    #print(jax)
    #print(caleb)
    patrick = {}
    patrick['carries'] = 200
    patrick['rushyds'] = 1990
    patrick['rushtds'] = 0
    henry = {'carries': 10000, 'rushyds': 20000, 'rushtds': 5000}
    #print(patrick)
    #print(henry)
    totalstats = {}
    totalstats['jax'] = jax
    totalstats['caleb'] = caleb
    totalstats['patrick'] = patrick
    totalstats['henry'] = henry
    #print(totalstats)
    # .keys()
    #print(totalstats.keys())
    #print(jax.keys())
    '''
    {'jax': {'carries': 100, 'rushyds': 1500, 'rushtds': 10}, 
      'caleb': {'carries': 101, 'rushyds': 1501, 'rushtds': 11}, 
      'patrick': {'carries': 200, 'rushyds': 1990, 'rushtds': 0}, 
      'henry': {'carries': 10000, 'rushyds': 20000, 'rushtds': 5000}
      }
    '''
    mostyds = 0
    for key in totalstats.keys():
        if totalstats[key]['rushyds'] > mostyds:
            maxname = key
            mostyds = totalstats[key]['rushyds']
    print(maxname, mostyds)

    newdictionary = {'jax': 1500, 'caleb': 1501, 'patrick': 1990, 'henry': 20000}
    sorteddictionary = sorted(newdictionary.items(), key=lambda x: x[1], reverse=True)
    print(sorteddictionary[0])

if __name__ == "__main__":
    football()