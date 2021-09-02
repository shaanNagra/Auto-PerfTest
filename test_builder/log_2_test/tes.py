import lxml.etree as ET
import constants
import BasicElementBuilder
import jsr223SamplerBuilder
import jmeterTestPlanBuilder
import threadGroupBuilder
import testPlanBuilder

script = '''import com.keysolutions.*;
import com.keysolutions.ddpclient.*;
import java.util.*;


DDPClient client = new DDPClient(&quot;localhost&quot;, 3000)
log.info(&quot;\nWVWVWVWVWVWVWVVW &quot;+(client.connect()).toString());
vars.putObject(&quot;client&quot;,client);
Thread.sleep(1500);
'''

jmeterTP = jmeterTestPlanBuilder.jmeterTestPlanBuilder("1.2","5.0","5.4.1")
testplan = testPlanBuilder.testPlanBuilder()
threadGroup = threadGroupBuilder.threadGroupBuilder()
sampler = jsr223SamplerBuilder.jsr223SamplerBuilder()
sampler.configJSR223_Script(script=script)
jmeterTP.append(testplan.getElem())
threadGroup.append(sampler.getElem())
testplan.append(threadGroup.getElem())
jmeterTP.print()

file = open('testRunRes.jmx','wb')
file.write(jmeterTP.toString())
file.close()
