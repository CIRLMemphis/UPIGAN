"""
    author: SPDKH
"""
import datetime
import os
from data.data import Data
from utils import fcns


class FixedCell(Data):
    def __init__(self, args):
        Data.__init__(self, args)
        self.data_groups = {'train': 'training',
                            'test': 'testing',
                            'val': 'validation'}

        self.data_types = {'x': 'rawdata', 'y': 'gt'}
        self.args.data_dir = fcns.fix_path(self.args.data_dir)
        input_dir = os.path.join(self.args.data_dir,
                                 self.data_groups['train'],
                                 self.data_types['x'])
        output_dir = os.path.join(self.args.data_dir,
                                  self.data_groups['train'],
                                  self.data_types['y'])
        in_sample_dir = os.path.join(input_dir,
                                     os.listdir(input_dir)[0])
        self.input_dim = self.load_sample(in_sample_dir)
        print('input', self.input_dim)
        out_sample_dir = os.path.join(output_dir,
                                      os.listdir(output_dir)[0])

        self.output_dim = self.load_sample(out_sample_dir)
        print('output', self.output_dim)

        # if not os.path.exists(self.log_path):
        # check_folder(self.log_path)

        for data_group in self.data_groups.keys():
            self.data_dirs[data_group] = os.path.join(self.args.data_dir,
                                                      self.data_groups[data_group])
            for data_type in self.data_types.keys():
                self.data_dirs[data_type + data_group] = \
                    os.path.join(self.data_dirs[data_group],
                                 self.data_types[data_type])
        print(self.data_dirs)

        # self.otf_path = './OTF/fixed_cell_otf.tif'
        self.otf_path = './OTF/splinePSF_128_128_11.mat'
        # self.psf = self.init_psf()
