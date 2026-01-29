import json
from urllib.parse import urljoin
from pathlib import Path


class Component:
    BASE_URL = "https://transport.api.ltnglobal.com/v1/"
    _json_key = None

    def __init__(self, name, session):
        self.name = name
        self.session = session
        self.url = urljoin(self.BASE_URL, self._json_key)

    def get_info(self):
        if self._json_key:
            return self.session.get(self.url, params=self.search_filter).json()[self._json_key]
        else:
            return self.session.get(self.url, params=self.search_filter).json()



class Channel(Component):
    _json_key = "channels"

    def __init__(self, name, session):
        super().__init__(name, session)
        self.search_filter = {
            "filter": f'channel_id=\'{self.name}\'',
            "page_size": 999999
        }


class Leaf(Component):
    _json_key = "leaves"

    def __init__(self, name, session, filter_by):
        super().__init__(name, session)
        self.filter_by = filter_by
        self.search_filter = {
            "filter": f'{self.filter_by}=\'{self.name}\'',
            "page_size": 999999
        }

    def create_decoder_confs(self):
        base_dir = Path.home() / "decoder_confs" / self.get_info()[0]['endpoint_id']

        base_dir.mkdir(parents=True, exist_ok=True)

        count = 0

        for decoder in self.get_info():
            try:
                if '8' in decoder['tag_ids'] and decoder['leaf_type'] == 'DEST':
                    decoder_num = decoder['leaf_id'].split('-d')[-1]
                    filename = f"decoder{decoder_num}.conf"

                    file_path = base_dir / filename

                    mcast_addr = decoder['transport_handoff_ip']
                    mcast_port = decoder['transport_handoff_port']
                    count += 1
                    file_path.write_text(f"SEND_ADDRESS1={mcast_addr}:{mcast_port}")
                    Path(file_path).chmod(0o664)
            except Exception as e:
                pass
                #print(f"Failure: {e}, {decoder['leaf_id']}")
        print(f"Success: {count} decoder confs have been created at {base_dir}")


class Endpoint(Component):
    _json_key = "endpoints"

    def __init__(self, name, session):
        super().__init__(name, session)
        self.search_filter = {
            "filter": f'endpoint_id=\'{self.name}\'',
            "page_size": 999999
        }


class Overlay(Component):
    _json_key = "overlay_server_pairs"

    def __init__(self, name, session):
        super().__init__(name, session)
        self.search_filter = {
            "filter": f'overlay=\'{self.name}\'',
            "page_size": 999999
        }


class Flowclient(Component):
    _json_key = "flowclients"

    def __init__(self, name, session, filter_by):
        super().__init__(name, session)
        self.filter_by = filter_by
        self.search_filter = {
            "filter": f'{self.filter_by}=\'{self.name}\'',
            "page_size": 999999
        }


class Hardware(Component):
    _json_key = "hardware"

    def __init__(self, name, session, filter_by):
        super().__init__(name, session)
        self.filter_by = filter_by
        self.search_filter = {
            "filter": f"{self.filter_by}=\'{self.name}\'",
            "page_size": 999999
        }


class Appliances(Component):
    _json_key = "appliances"

    def __init__(self, name, session, filter_by):
        super().__init__(name, session)
        self.filter_by = filter_by
        self.search_filter = {
            "filter": f"{self.filter_by}=\'{self.name}\'",
            "page_size": 999999
        }

