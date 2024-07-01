python_requirement(
    name="setuptools",
    requirements=["setuptools"],
)
python_requirement(
    name="python-multipart",
    requirements=["python-multipart==0.0.6"],
    modules=["multipart"],
)

python_requirements(
    name="local_reqs",
    source="dev-requirements.txt",
    overrides={
        "mongomock-motor": {"dependencies": [":setuptools"]},
    },
)

python_requirements(
    name="requirements",
    source="requirements.txt",
    overrides={
        "fastapi": {"dependencies": [":python-multipart"]},
        "uvicorn": {"dependencies": [":requirements#uvloop", ":requirements#httptools"]},
        "pypdfium2": {"dependencies": [":requirements#Pillow"]},
    },
    module_mapping={
        "pyyaml": ["yaml"],
        "Pillow": ["PIL"],
    },
    type_stubs_module_mapping={
        "types-PyYAML": ["yaml"],
    },
)

python_requirement(name="ruff", requirements=["ruff==0.3.0"], resolve="ruff")
