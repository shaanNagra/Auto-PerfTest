# *AUTO - PERF TEST*
*(a work in progress title)*

## File Structure
* as of 20th august 2021
* [made using VScode Extension](https://marketplace.visualstudio.com/items?itemName=Shinotatwu-DS.file-tree-generator)
```
Auto-PerfTest
 ┃
 ┣ DDP-sampler
 ┃ ┣ README.md
 ┃ ┣ ddp-sampler-tests.js
 ┃ ┣ ddp-sampler.js
 ┃ ┣ get-methods.js
 ┃ ┗ packages.js
 ┃
 ┣ Extras
 ┃
 ┣ autonomic_loadtester
 ┃ ┃
 ┃ ┣ db_functions
 ┃ ┃ ┣ __pycache__
 ┃ ┃ ┃ ┗ db_constants.cpython-38.pyc
 ┃ ┃ ┣ db_api_cluster.py
 ┃ ┃ ┣ db_api_group.py
 ┃ ┃ ┣ db_conn.py
 ┃ ┃ ┣ db_constants.py
 ┃ ┃ ┣ db_init_app.py
 ┃ ┃ ┗ db_init_database.py
 ┃ ┃
 ┃ ┣ extra_data
 ┃ ┃
 ┃ ┣ session_listener
 ┃ ┃ ┃
 ┃ ┃ ┣ extra
 ┃ ┃ ┃ ┣ initCollection.js
 ┃ ┃ ┃ ┣ initDB.js
 ┃ ┃ ┃ ┗ webapp.js
 ┃ ┃ ┃
 ┃ ┃ ┣ node_modules
 ┃ ┃ ┃ ┗ ...
 ┃ ┃ ┃
 ┃ ┃ ┣ app.js
 ┃ ┃ ┣ open.js
 ┃ ┃ ┣ package.json
 ┃ ┃ ┗ session.js
 ┃ ┃
 ┃ ┣ test_builder
 ┃ ┃ ┃
 ┃ ┃ ┣ Extras
 ┃ ┃ ┃ ┣ Graphs
 ┃ ┃ ┃ ┗ notebook.ipynb
 ┃ ┃ ┃
 ┃ ┃ ┣ log_2_test
 ┃ ┃ ┃ ┣ BasicElementBuilder.py
 ┃ ┃ ┃ ┣ constants.py
 ┃ ┃ ┃ ┣ elemBuilder.py
 ┃ ┃ ┃ ┣ functions.py
 ┃ ┃ ┃ ┣ jmeterTestPlanBuilder.py
 ┃ ┃ ┃ ┣ jsr223SamplerBuilder.py
 ┃ ┃ ┃ ┣ temp.py
 ┃ ┃ ┃ ┣ testPlanBuilder.py
 ┃ ┃ ┃ ┣ testRun.py
 ┃ ┃ ┃ ┣ testRunRes.jmx
 ┃ ┃ ┃ ┣ thinkTimeBuilder.py
 ┃ ┃ ┃ ┣ threadGroupBuilder.py
 ┃ ┃ ┃ ┗ wrapper.py
 ┃ ┃ ┃ 
 ┃ ┃ ┣ session_clusterer
 ┃ ┃ ┃ ┣ Analyzer.py
 ┃ ┃ ┃ ┗ callClusterer.py
 ┃ ┃ ┃
 ┃ ┃ ┣ session_grouper
 ┃ ┃ ┃ ┣ comparison.py
 ┃ ┃ ┃ ┗ grouping.py
 ┃ ┃ ┃
 ┃ ┃ ┗ sequentialProcess.py
 ┃ ┃
 ┃ ┣ test_executer
 ┃ ┗ test_manager
 ┃
 ┗ README.md
```

## Links
| folders        | Content            |
| :------------- | ------------------ |
| not setup    |[link](https://github.com/shaanNagra/)|




```
db.getCollection('sessions').aggregate([{
    '$lookup': {
        'from':"sessionsOps",
        'localField':'_id',
        'foreignField':'session_id',
        'as':'log'
        }
     }
     ])
```