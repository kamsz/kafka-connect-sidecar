import requests
import json
import logging as log
import glob
from time import sleep


def main():
    log.basicConfig(level=log.INFO)

    while True:
        log.info('Reading connectors')

        connectors = []

        for definition in glob.glob('/connectors/*.json'):
            log.info('Reading connector definition from {}'.format(definition))
            with open(definition) as stream:
                connectors.append(json.loads(stream.read()))

        log.info('Updating Kafka Connect')

        for connector in connectors:
            log.info('Connector definition: {}'. format(connector))
            log.info('Checking if connector is already defined')

            try:
                resp = requests.get(
                    'http://localhost:8083/connectors/{}'.format(connector['name']))
            except Exception as e:
                log.error(e)
                continue

            log.info('Received: {}'.format(resp.status_code))

            if resp.status_code == 200:
                log.info('Updating connector definition')

                try:
                    resp = requests.put(
                        'http://localhost:8083/connectors/{}/config'.format(connector['name']), json=connector['config'])
                except Exception as e:
                    log.error(e)
                    continue

                log.info('Received: {}'.format(resp.status_code))
            elif resp.status_code == 404:
                log.info('Creating connector')

                try:
                    resp = requests.post(
                        'http://localhost:8083/connectors', json=connector)
                except Exception as e:
                    log.error(e)
                    continue

                log.info('Received: {}'.format(resp.status_code))

        log.info('Sleeping for 60s')
        sleep(60)


main()
