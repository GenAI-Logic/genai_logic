# Welcome to GenAI-Logic

Thankyou for installing!  We very much appreciate your interest, and are determined to make your experience as productive as possible.

Issues?  Email us at `support@genai-logic.com`

&nbsp;

## Install GenAI-Logic and WebGenAI

To install WebGenAI:

1. Copy the license file you received in the registration email over this: `webgenai/webg_config/license`.json 
2. GenAI-Logic uses OpenAI, which requires an Open API Key:
    1. Obtain a Key
        1. Obtain one from [here](https://platform.openai.com/account/api-keys) or [here](https://platform.openai.com/api-keys)
        2. Authorize payments [here](https://platform.openai.com/settings/organization/billing/overview)
        3. Create an environmental variable `APILOGICSERVER_CHATGPT_MODEL`
    2. Update this file with your OpenAI API Key: `webgenai/webg_config/web_genai.txt`.

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

Installation not required.

Your install includes a few sample systems at: samples.

To run the default sample:

```bash
sh run_sample nw_sample
```

To run a different sample, replace `nw_sample` with the sample directory.  Only 1 sample can be running at a time.

| Sample | Notes   |
| :------------- | :------------- |
| nw_sample | Our take on Northwind (Customers, Orders etc), **with logic.**<br>&nbsp;&nbsp;&nbsp;&nbsp;1. Illustrates key functionality<br>&nbsp;&nbsp;&nbsp;&nbsp;2. Extensive [Tutorial](https://apilogicserver.github.io/Docs/Tutorial/) and code/logic examples |
| nw_sample_nocust | Uncustomized version of nw, created in about 5-10 seconds.<br>&nbsp;&nbsp;&nbsp;&nbsp;* Illustrates results you should obtain using your existing databases |

&nbsp;

## Creating projects from existing databases

TBD

&nbsp;

## Debugging Projects in VSCode

TBD