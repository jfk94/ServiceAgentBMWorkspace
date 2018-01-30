#!/bin/bash

vagrant box add seek/ubuntu-14.04-desktop
vagrant init seek/ubuntu-14.04-desktop --box-version 1.0.0
vagrant up --provider virtualbox
