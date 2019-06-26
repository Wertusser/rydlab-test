from flask_restful import Resource, marshal_with
from gist.fields.statistic import stats_fields
from gist.models import File
from collections import Counter
import math


class Statistic(Resource):
    @marshal_with(stats_fields, envelope="result")
    def get(self):
        ext = [file.extension for file in File.select(File.extension)]
        amount = len(ext)
        result = [{"name": i[0], "amount": math.floor(i[1] / amount * 100)} for i in Counter(ext).most_common()]
        return {"langs": result}, 200
