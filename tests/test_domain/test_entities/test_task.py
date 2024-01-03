from domain.entities.task.task import Task


    
def test_create_task():
    task = Task(1, 'Задача', 'Выполнить задание', 'В процессе' )
    assert  task.id == 1
    assert  task.title == 'Задача'
    assert  task.description == 'Выполнить задание'
    assert task.status == 'В процессе'