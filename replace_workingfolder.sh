#!/bin/sh

sed -i 's/\/area1\/obigo\/SA/${PWD}/' $1
sed -i 's/export OBIGO_SA_LIB_DIR=${OBIGO_SA_DIR}\/lib/export OBIGO_SA_LIB_DIR=${OBIGO_SA_DIR}\/lib:\/area1\/obigo\/SA\/lib/' $1
