import streamlit as st
import pandas as pd
import numpy as np

st.set_option('deprecation.showPyplotGlobalUse', False)

st.title('Relife App - Get to know survival analysis biases')

st.image("data:image/png;base64,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")

st.write("""
ReLife is an open source Python library for asset management based on reliability theory and lifetime data analysis.

- Survival analysis: non-parametric estimator (Kaplan-Meier), parametric estimator (Maximum Likelihood) and regression models (Accelerated Failure Time and Parametric Proportional Hazards) on left-truncated, right-censored and left-censored lifetime data.

- Reliability theory: optimal age of replacement for time-based mainteance policy for one-cycle or infinite number of cycles, with exponential discounting.

- Renewal theory: expected number of events, expected total costs or expected number of replacements for run-to-failures or age replacement policies.

The official documentation is available [here](https://rte-france.github.io/relife/).


Survivorship bias or survival bias is the logical error of concentrating on entities that passed a selection process while overlooking those that did not. This can lead to incorrect conclusions because of incomplete data.

Survivorship bias is a form of selection bias that can lead to overly optimistic beliefs because multiple failures are overlooked, such as when companies that no longer exist are excluded from analyses of financial performance. It can also lead to the false belief that the successes in a group have some special property, rather than just coincidence as in correlation "proves" causality.

Another kind of survivorship bias would involve thinking that an incident was not all that dangerous because the only people who were involved in the incident who can speak about it are those who survived it. Even if one knew that some people are dead, they would not have their voice to add to the conversation, leading to bias in the conversation. 
""")

import numpy as np
import matplotlib.pyplot as plt
from relife.datasets import load_circuit_breaker
from relife import KaplanMeier, Weibull, Gompertz, AgeReplacementPolicy

time, event, entry = load_circuit_breaker().astuple()
km = KaplanMeier().fit(time,event,entry)
weibull = Weibull().fit(time,event,entry)
gompertz = Gompertz().fit(time,event,entry)

km.plot()
weibull.plot()
gompertz.plot()
plt.xlabel('Age [year]')
plt.ylabel('Survival probability')

st.pyplot()

a0 = np.array([15, 20, 25]).reshape(-1,1)
cp = 10
cf = np.array([900, 500, 100]).reshape(-1,1)
policy = AgeReplacementPolicy(gompertz, a0=a0, cf=cf, cp=cp, rate=0.04)
policy.fit()
st.table(policy.ar1)
st.table(policy.ar)

a = np.arange(1,100,0.1)
za = policy.asymptotic_expected_equivalent_annual_cost(a)
za_opt = policy.asymptotic_expected_equivalent_annual_cost()
plt.plot(a, za.T)
for i, ar in enumerate(policy.ar):
    plt.scatter(ar, za_opt[i], c=f'C{i}', label=f" cf={cf[i,0]} k€, ar={ar[0]:0.1f} years")
plt.xlabel('Age of preventive replacement [years]')
plt.ylabel('Asymptotic expected equivalent annual cost [k€]')
plt.legend()

st.pyplot()
