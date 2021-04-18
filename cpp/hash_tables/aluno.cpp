#include "aluno.h"

Aluno::Aluno() {
  this->ra = -1;
  this->nome = "";
}

Aluno::Aluno::getNome() const {
  return nome;
}

Aluno::Aluno::getRa() const {
  return ra;
}
