from sqlalchemy.orm import sessionmaker, Session
from sqlalchemy.engine import create_engine, Engine

from types import TracebackType

class SessionManager:

    """Responsável por lidar com o ciclo de vida transacional do banco de dados"""

    def __init__(self, database_url: str) -> None:

        """Inicializa os atributos de instância da classe SessionManager

        Parameters
        ----------

        database_url: str
            URL do banco de dados usado pela Engine

        """

        self.__engine: Engine = create_engine(database_url)
        self.__session = None
    
    @property
    def session(self) -> Session:

        """Obtém a sessão atual do gerenciador

        Returns
        -------
        Session
            sessão atual do gerenciador
        """

        return self.__session
    
    def __enter__(self) -> "SessionManager":

        """Cria uma sessão a partir da entrada de um gerenciador de contexto

        Returns
        -------
        SessionManager
            Objeto com a sessão criada
        """

        # Fábrica de sessões associada a uma conexão
        session_maker = sessionmaker(bind=self.__engine)

        # Sessão criada com a fábrica
        self.__session = session_maker()
        
        return self

    def __exit__(self, exc_type: type[BaseException] | None, exc_value: BaseException | None, exc_tb: TracebackType | None) -> None:

        """Finaliza uma sessão a partir da saída de um gerenciador de contexto

        Parameters
        ----------
        exc_type: type[BaseException] | None
            O tipo da exceção levantada no contexto

        exc_value: BaseException | None
            Valor da exceção levantada no contexto

        exc_traceback: TracebackType | None
            Traceback da exceção levantada no contexto
            
        """

        if exc_type:

            self.__session.rollback() # Rollback nas transações
        
        else:

            self.__session.commit() # Persiste as transações

        self.__session.close()