Running CoverUp-Eval

- check out coverup-eval repository

```
    git clone --recurse-submodules git@github.com:plasma-umass/coverup-eval
    cd coverup-eval
```

- set up pip cache (to speed up module installations)

```
    mkdir pip-cache
    sudo chown root:root pip-cache
```

- load docker image

```
    bunzip2 docker/coverup-runner.tar.bz2
    docker load <docker/coverup-runner.tar
```

- add any keys

```
    vim config/common.sh    # add any keys here, or add them to your-new-model.sh below
```

- add configuration. This will be a new file; see config/default.sh for an example

```
    echo COVERUP_ARGS=\"--model your-new-model\" > config/your-new-model.sh
```

- run CoverUp on a first benchmark to try it out

```
    python3 scripts/eval_coverup.py --config your-new-model flutils
```

- if things look good, let it run on the others (it will skip any already done)

```
    python3 scripts/eval_coverup.py --config your-new-model >coverup-your-new-model.log 2>&1 &
```

- check the results, for example, with

```
    python3 scripts/compare.py --config your-new-model
```

`compare.py` compares two systems.
It assumes that the first one is CoverUp (with GPT-4),
but you can change that one's configuration using `--config`.
By default, it compares `--to codamosa-gpt4`,
but you can have it compare to any `coverup-...` where `...` is the configuration name.
  
