# -*- coding: utf-8 -*-
import logging
from typing import List

from airflow_munchkin.block_generator import hook_generator
from airflow_munchkin.block_generator.blocks import FileBlock
from airflow_munchkin.client_parser import ClientInfo
from airflow_munchkin.integration import Integration


def generate_file_blocks(
    client_info: ClientInfo, integration: Integration
) -> List[FileBlock]:
    logging.info("Start generating file blocks")
    hook_file_block = hook_generator.create_file_block(client_info, integration)
    logging.info("Finish generating file blocks")

    return [hook_file_block]