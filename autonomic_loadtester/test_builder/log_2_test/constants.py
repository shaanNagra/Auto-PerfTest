
import lxml.etree as ET


TEST_PLAN =  '<TestPlan guiclass="TestPlanGui" testclass="TestPlan" testname="LOGINAPPTESTPLAN" enabled="true">'\
      '<stringProp name="TestPlan.comments"></stringProp>'\
      '<boolProp name="TestPlan.functional_mode"></boolProp>'\
      '<boolProp name="TestPlan.tearDown_on_shutdown"></boolProp>'\
      '<boolProp name="TestPlan.serialize_threadgroups"></boolProp>'\
      '<elementProp name="TestPlan.user_defined_variables" elementType="Arguments" guiclass="ArgumentsPanel" testclass="Arguments" testname="User Defined Variables" enabled="true">'\
        '<collectionProp name="Arguments.arguments"/>'\
      '</elementProp>'\
      '<stringProp name="TestPlan.user_define_classpath"></stringProp>'\
    '</TestPlan>'

THREAD_GROUP = '<ThreadGroup guiclass="ThreadGroupGui" testclass="ThreadGroup" testname="Thread Group" enabled="true">' \
        '<stringProp name="ThreadGroup.on_sample_error">continue</stringProp>' \
        '<elementProp name="ThreadGroup.main_controller" elementType="LoopController" guiclass="LoopControlPanel" testclass="LoopController" testname="Loop Controller" enabled="true">' \
          '<boolProp name="LoopController.continue_forever">false</boolProp>' \
          '<stringProp name="LoopController.loops">1</stringProp>'\
        '</elementProp>'\
        '<stringProp name="ThreadGroup.num_threads">1</stringProp>'\
        '<stringProp name="ThreadGroup.ramp_time">1</stringProp>'\
        '<boolProp name="ThreadGroup.scheduler">false</boolProp>'\
        '<stringProp name="ThreadGroup.duration"></stringProp>'\
        '<stringProp name="ThreadGroup.delay"></stringProp>'\
        '<boolProp name="ThreadGroup.same_user_on_next_iteration">false</boolProp>'\
      '</ThreadGroup>'

CSV_DATA_SET_CONFIG = '<CSVDataSet guiclass="TestBeanGUI" testclass="CSVDataSet" testname="CSV Data Set Config" enabled="true">'\
          '<stringProp name="delimiter">,</stringProp>'\
          '<stringProp name="fileEncoding">UTF-8</stringProp>'\
          '<stringProp name="filename">/home/shaan/Documents/CSVSample_user.csv</stringProp>'\
          '<boolProp name="ignoreFirstLine">false</boolProp>'\
          '<boolProp name="quotedData">false</boolProp>'\
          '<boolProp name="recycle">true</boolProp>'\
          '<stringProp name="shareMode">shareMode.all</stringProp>'\
          '<boolProp name="stopThread">false</boolProp>'\
          '<stringProp name="variableNames">user,password</stringProp>'\
        '</CSVDataSet>'

JSR223_SAMPLER = '<JSR223Sampler guiclass="TestBeanGUI" testclass="JSR223Sampler" testname="JSR223 Sampler" enabled="true">'\
          '<stringProp name="cacheKey">true</stringProp>'\
          '<stringProp name="filename"></stringProp>'\
          '<stringProp name="parameters"></stringProp>'\
          '<stringProp name="script"></stringProp>'\
          '<stringProp name="scriptLanguage">groovy</stringProp>'\
        '</JSR223Sampler>'

ONCE_ONLY_CONTROLLER = '<OnceOnlyController guiclass="OnceOnlyControllerGui" testclass="OnceOnlyController" testname="Once Only Controller" enabled="true"/>'

THINK_TIME =  '<TestAction guiclass="TestActionGui" testclass="TestAction" testname="Think Time" enabled="true">'\
                '<intProp name="ActionProcessor.action">1</intProp>'\
                '<intProp name="ActionProcessor.target">0</intProp>'\
                '<stringProp name="ActionProcessor.duration">0</stringProp>'\
              '</TestAction>'

UNIFORM_RANDOM_TIMER =  '<UniformRandomTimer guiclass="UniformRandomTimerGui" testclass="UniformRandomTimer" testname="Pause" enabled="true">'\
                          '<stringProp name="ConstantTimer.delay">1000</stringProp>'\
                          '<stringProp name="RandomTimer.range">100</stringProp>'\
                        '</UniformRandomTimer>'


RANDOM_CONTROLLER = '<RandomController guiclass="RandomControlGui" testclass="RandomController" testname="Random Controller" enabled="true">'\
                      '<intProp name="InterleaveControl.style">1</intProp>'\
                    '</RandomController>'

HASH_TREE = '<hashTree/>'