# CoverUp Replication Package
This artifact accompanies the [FSE'25](https://conf.researchr.org/home/fse-2025) accepted paper,
"CoverUp: Effective High Coverage Test Generation for Python"
by Juan Altmayer Pizzorno <jpizzorno@cs.umass.edu> and Emery D. Berger <emery@cs.umass.edu>.

## Table of Contents
- README.md (this document) contains general and usage information for this artifact;
- [LICENSE] describes distribution rights;

## Requirements
CoverUp has its own [repository on GitHub](https://github.com/plasma-umass/coverup);
If you are only looking to use it, please follow the instructions on that repository.

The evaluation scripts require Python 3.10+.
Running CoverUp on the evaluation suites requires Docker; all instructions assume a Linux system.

## Obtaining a Local Copy
```
    git clone --recurse-submodules git@github.com:plasma-umass/coverup-eval
    cd coverup-eval
```

# Understanding Configurations and Suites
CoverUp's evaluation compares it to CodaMosa and MuTAP
TODO explain configurations, suites, etc.

## Viewing Results
- Use `scripts/compare.py` to compare CoverUp results to a second system.
The first system must always be CoverUp, but you can select its configuration with `--config`.
Specify the system to compare against using `--to` and the evaluation suite with `--suite`.

- check the results, for example, with
```
    python3 scripts/compare.py --config your-new-model
```

`compare.py` compares two systems.
It assumes that the first one is CoverUp (with GPT-4o),
but you can change that one's configuration using `--config`.
By default, it compares `--to codamosa-gpt4o`,
but you can have it compare to any `coverup-...` where `...` is the configuration name.

## Running CoverUp's Evaluation on a New (or Existing) Configuration
- Set up pip cache (to speed up module installations)
```
    mkdir pip-cache
    sudo chown root:root pip-cache
```

- Load docker image
```
    bunzip2 docker/coverup-runner.tar.bz2
    docker load <docker/coverup-runner.tar
```

- Add any keys needed (from OpenAI or elsewhere) to `config/common.sh` or `your-new-model.sh` below. `config/common.sh` is always included and is in `.gitignore` to help avoid checking it in by mistake.
```
    vim config/common.sh
```

- Create a new configuration. This will be a new file; see `config/default.sh` for an example
```
    echo COVERUP_ARGS=\"--model your-new-model\" > config/your-new-model.sh
```

- Run CoverUp on a first benchmark (here, `flutils`) to try it out
```
    python3 scripts/eval_coverup.py --config your-new-model flutils
```

- If things look good, let it run on the others (it will skip any that are already done)
```
    python3 scripts/eval_coverup.py --config your-new-model >coverup-your-new-model.log 2>&1 &
```
