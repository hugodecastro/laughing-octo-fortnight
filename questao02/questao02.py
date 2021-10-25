# -*- coding: utf-8 -*-
import apache_beam as beam
import json

p1 = beam.Pipeline()

class parse_json(beam.DoFn):

    def process(self, record):
        """
            Retorna o seguinte JSON:
            {
                "title": "Floor Access Event",
                "type": "object",
                "properties": {
                    "person_id": {
                        "type": "string"
                    },
                    "datetime": {
                        "type": "string",
                        "format": "date-time"
                    },
                    "floor_level": {
                        "type": "integer"
                    },
                    "building": {
                        "type": "string"
                    }
                },
                "required": ["person_id", "datetime", "floor_level", "building"]
            }
        """
        person_id = record[0]
        date_time = record[1].replace("/","-")
        floor_level = int(record[2])
        building = record[3]
        yield {
            "title": "Floor Access Event",
            "type": "object",
            "properties": {
                "person_id": person_id,
                "datetime": date_time,
                "floor_level": floor_level,
                "building": building
            },
            "required": ["person_id", "datetime", "floor_level", "building"]
        }

FloorAccess = (
  p1
  | "Importar Dados Painel Casos" >> beam.io.ReadFromText(r"[PATH-TO-FILE]/questao_02.csv", skip_header_lines = 1)
  | "Separar por , ..." >> beam.Map(lambda record: record.split(','))
  | "Mapeando entradas" >> beam.ParDo(parse_json())
  | "Saída" >> beam.io.WriteToText(file_path_prefix=r"[PATH-TO-EXIT]/result",
                                            file_name_suffix='.json',
                                            shard_name_template='')
  
)


p1.run()