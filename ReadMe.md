# Introduction to Flask
## Codeup - Bayes Cohort

<h1 id="virtual-environments">Virtual Environments</h1>
<p>Virtual environments let us isolate project dependencies, that is, the third
party libraries we use with each project. For example, if one project you are
working on depends on an older version of pandas, but you want to use the newest
version elsewhere, we could create seperate virtual environments for each
project.</p>
<h2 id="creating-a-virtual-environment">Creating a Virtual Environment</h2>
<ol>
<li>
<p>Create a virtual environment</p>
<div class="highlight"><pre><span></span>python -m venv env
</pre></div>

<p>Where <code>env</code> is the name of the directory to create the virtual environment
inside of. We'll assume you are also using <code>env</code> for the rest of the
examples.</p>
</li>
<li>
<p>Add the <code>env</code> directory to your <code>.gitignore</code>.</p>
</li>
<li>
<p>Activate the virtual environment</p>
<div class="highlight"><pre><span></span>source env/bin/activate
</pre></div>

<p>From this point forward, your shell will exist inside the virtual
environment.</p>
</li>
</ol>
<h2 id="installing-dependencies">Installing Dependencies</h2>
<div class="admonition note">
<p class="admonition-title">Virtual Environments</p>
<p>Each virtual environment is seperate from all the others, and also separate
from your "global" python installation. Just because you've installed a
library elsewhere, doesn't mean it will be available in a new virtual
environment. Any libraries you plan on using must be explicitly installed.</p>
</div>
<ol>
<li>
<p>Make sure the virtual environment is activated.</p>
</li>
<li>
<p>(If a <code>requirements.txt</code> file exists) Install any existing dependencies.</p>
<div class="highlight"><pre><span></span>python -m pip install -r requirements.txt
</pre></div>

</li>
<li>
<p>Add a new dependency.</p>
<div class="highlight"><pre><span></span>python -m pip install sklearn
</pre></div>

</li>
<li>
<p>Save all your installed dependencies to a text file.</p>
<div class="highlight"><pre><span></span>python -m pip freeze &gt; requirements.txt
</pre></div>

</li>
</ol>
<h2 id="workflow">Workflow</h2>
<h3 id="setting-up-a-new-project">Setting up a New Project</h3>
<ol>
<li>Create the virutal environment.</li>
<li>Install dependencies with pip.</li>
<li>Save the dependencies to <code>requirements.txt</code>.</li>
</ol>
<h3 id="starting-work-on-an-existing-project">Starting Work on an Existing Project</h3>
<ol>
<li>
<p>Activate the virtual environment</p>
</li>
<li>
<p>Install the project dependencies from <code>requirements.txt</code></p>
<div class="highlight"><pre><span></span>pip install -r requirements.txt
</pre></div>

</li>
</ol>
<h3 id="day-to-day-project-work">Day-to-day project work</h3>
<ol>
<li>Activate the virtual environment.</li>
<li>Work on your project like you normally would.</li>
<li>Deactivate the virtual environment when you are done working on the project.</li>
</ol>