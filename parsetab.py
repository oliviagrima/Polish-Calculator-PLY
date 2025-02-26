
# parsetab.py
# This file is automatically generated. Do not edit.
# pylint: disable=W,C,R
_tabversion = '3.10'

_lr_method = 'LALR'

_lr_signature = 'BINARIO COS DIV ENTERO EXP HEXADECIMAL LOG MAS MENOS MULT NEG REAL SIN\n        expresion : MAS expresion expresion\n                   | MENOS expresion expresion \n                   | MULT expresion expresion \n                   | DIV expresion expresion \n        \n        expresion : NEG expresion\n                   | EXP expresion\n                   | LOG expresion\n                   | SIN expresion\n                   | COS expresion\n        \n        expresion : ENTERO\n                    | REAL\n                    | BINARIO\n                    | HEXADECIMAL\n        '
    
_lr_action_items = {'MAS':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,],[2,2,2,2,2,2,2,2,2,2,-10,-11,-12,-13,2,2,2,2,-5,-6,-7,-8,-9,-1,-2,-3,-4,]),'MENOS':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,],[3,3,3,3,3,3,3,3,3,3,-10,-11,-12,-13,3,3,3,3,-5,-6,-7,-8,-9,-1,-2,-3,-4,]),'MULT':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,],[4,4,4,4,4,4,4,4,4,4,-10,-11,-12,-13,4,4,4,4,-5,-6,-7,-8,-9,-1,-2,-3,-4,]),'DIV':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,],[5,5,5,5,5,5,5,5,5,5,-10,-11,-12,-13,5,5,5,5,-5,-6,-7,-8,-9,-1,-2,-3,-4,]),'NEG':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,],[6,6,6,6,6,6,6,6,6,6,-10,-11,-12,-13,6,6,6,6,-5,-6,-7,-8,-9,-1,-2,-3,-4,]),'EXP':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,],[7,7,7,7,7,7,7,7,7,7,-10,-11,-12,-13,7,7,7,7,-5,-6,-7,-8,-9,-1,-2,-3,-4,]),'LOG':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,],[8,8,8,8,8,8,8,8,8,8,-10,-11,-12,-13,8,8,8,8,-5,-6,-7,-8,-9,-1,-2,-3,-4,]),'SIN':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,],[9,9,9,9,9,9,9,9,9,9,-10,-11,-12,-13,9,9,9,9,-5,-6,-7,-8,-9,-1,-2,-3,-4,]),'COS':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,],[10,10,10,10,10,10,10,10,10,10,-10,-11,-12,-13,10,10,10,10,-5,-6,-7,-8,-9,-1,-2,-3,-4,]),'ENTERO':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,],[11,11,11,11,11,11,11,11,11,11,-10,-11,-12,-13,11,11,11,11,-5,-6,-7,-8,-9,-1,-2,-3,-4,]),'REAL':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,],[12,12,12,12,12,12,12,12,12,12,-10,-11,-12,-13,12,12,12,12,-5,-6,-7,-8,-9,-1,-2,-3,-4,]),'BINARIO':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,],[13,13,13,13,13,13,13,13,13,13,-10,-11,-12,-13,13,13,13,13,-5,-6,-7,-8,-9,-1,-2,-3,-4,]),'HEXADECIMAL':([0,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,],[14,14,14,14,14,14,14,14,14,14,-10,-11,-12,-13,14,14,14,14,-5,-6,-7,-8,-9,-1,-2,-3,-4,]),'$end':([1,11,12,13,14,19,20,21,22,23,24,25,26,27,],[0,-10,-11,-12,-13,-5,-6,-7,-8,-9,-1,-2,-3,-4,]),}

_lr_action = {}
for _k, _v in _lr_action_items.items():
   for _x,_y in zip(_v[0],_v[1]):
      if not _x in _lr_action:  _lr_action[_x] = {}
      _lr_action[_x][_k] = _y
del _lr_action_items

_lr_goto_items = {'expresion':([0,2,3,4,5,6,7,8,9,10,15,16,17,18,],[1,15,16,17,18,19,20,21,22,23,24,25,26,27,]),}

_lr_goto = {}
for _k, _v in _lr_goto_items.items():
   for _x, _y in zip(_v[0], _v[1]):
       if not _x in _lr_goto: _lr_goto[_x] = {}
       _lr_goto[_x][_k] = _y
del _lr_goto_items
_lr_productions = [
  ("S' -> expresion","S'",1,None,None,None),
  ('expresion -> MAS expresion expresion','expresion',3,'p_exp_binaria','parser.py',15),
  ('expresion -> MENOS expresion expresion','expresion',3,'p_exp_binaria','parser.py',16),
  ('expresion -> MULT expresion expresion','expresion',3,'p_exp_binaria','parser.py',17),
  ('expresion -> DIV expresion expresion','expresion',3,'p_exp_binaria','parser.py',18),
  ('expresion -> NEG expresion','expresion',2,'p_exp_unaria','parser.py',36),
  ('expresion -> EXP expresion','expresion',2,'p_exp_unaria','parser.py',37),
  ('expresion -> LOG expresion','expresion',2,'p_exp_unaria','parser.py',38),
  ('expresion -> SIN expresion','expresion',2,'p_exp_unaria','parser.py',39),
  ('expresion -> COS expresion','expresion',2,'p_exp_unaria','parser.py',40),
  ('expresion -> ENTERO','expresion',1,'p_exp_numero','parser.py',60),
  ('expresion -> REAL','expresion',1,'p_exp_numero','parser.py',61),
  ('expresion -> BINARIO','expresion',1,'p_exp_numero','parser.py',62),
  ('expresion -> HEXADECIMAL','expresion',1,'p_exp_numero','parser.py',63),
]
