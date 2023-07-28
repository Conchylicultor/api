"""Generate the sphinx documentation."""

import apitree

apitree.make_project(
    modules={
        "jnp": "jax.numpy",
    },
    globals=globals(),
)
