from openmdao.api import PredeterminedRunsDriver


def get_desvar_path(design_variable):
    return 'designVariable.{}'.format(design_variable)


class CsvDriver(PredeterminedRunsDriver):
    def __init__(self, filename, *args, **kwargs):
        super(CsvDriver, self).__init__(*args, **kwargs)
        self.use_restart = False
        self.filename = filename

    def _deserialize_or_create_runlist(self):
        runlist = []
        with open(self.filename, 'rU') as csv_input:
            import csv
            reader = csv.reader(csv_input)
            header = next(iter(reader))
            indices = [i for i in range(len(header)) if get_desvar_path(header[i]) in self._desvars.keys()]

            def filter_desvar(l):
                """Filter out non-desvars (in case the .csv has other values)."""
                return (l[i] for i in indices)

            for values in reader:
                runlist.append(zip(map(get_desvar_path, filter_desvar(header)), filter_desvar(values)))
            return runlist
