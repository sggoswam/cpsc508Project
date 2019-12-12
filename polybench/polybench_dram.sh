#!/bin/bash

TEST_NAMES=("2mm_time"
    "3mm_time"
    "atax_time"
    "cholesky_time"
    "durbin_time"
    "lu_time"
    "trisolv_time"
    "gramschmidt_time")

for ((i = 0; i < ${#TEST_NAMES[@]}; ++i)); do
  perf stat -ddd -x '|' -e dtlb_load_misses.miss_causes_a_walk --append -o perf_results/${TEST_NAMES[i]}_dram.log bin/${TEST_NAMES[i]}
done