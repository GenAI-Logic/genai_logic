# Welcome to GenAI-Logic

## Install GenAI-Logic and WebGenAI

To install WebGenAI:

1. Copy the license file you received in the registration email over this: webgenai/webg_config/license.json 
2. GenAI-Logic uses OpenAI, which requires an Open API Key
    1. Obtain a Key
        1. Obtain one from [here](https://platform.openai.com/account/api-keys) or [here](https://platform.openai.com/api-keys)
        2. Authorize payments [here](https://platform.openai.com/settings/organization/billing/overview)
        3. Create an environmental variable `APILOGICSERVER_CHATGPT_MODEL`
    2. Update this file with your OpenAI API Key: webgenai/webg_config/web_genai.txt.  To get the key:

&nbsp;
## To Run WebGenAI

Once you have installed (above):

```bash
sh run_web_genai.sh
```

Open your [browser at](localhost:8282)

Find the [documentation here](https://apilogicserver.github.io/Docs/WebGenAI/)

&nbsp;

## Run API Logic Server samples 

Your install includes a few sample systems at: samples.

To run the default sample:

```bash
sh run_sample $
```

To run a different sample, replace $ with the sample directory.  Only 1 sample can be loaded at a time.

## Creating projects from existing databases

TBD

## Debugging Projects in VSCode

TBD