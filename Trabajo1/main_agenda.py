from agenda_contacto.agenda import Agenda

agenda = Agenda()


agenda.agregarContacto("Vicente", "987654321", "vicente@mail.com")
agenda.agregarContacto("Ana", "123456789", "ana@mail.com")


agenda.agregarContacto("Vicente", "000000000", "otro@mail.com")


agenda.buscarContacto("Vicente")
