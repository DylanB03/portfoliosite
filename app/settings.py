from pydantic_settings import BaseSettings, SettingsConfigDict
from pydantic import Field

class ConfigSettings(BaseSettings):

    web_host : str = Field(...,description="Host address for uvicorn server")

    web_port : int = Field(...,descriptoin="Port for uvicorn server")

    model_host : str = Field(...,description="Address for the LLM server")

    model_port : int = Field(...,description="Port for the LLM server")

    model_name : str = Field(...,description="Name of model to pull for LLM")

    mcp_host: str = Field(...,description="Address of mcp server")

    mcp_port: int = Field(...,description="Port of mcp server")

    email : str = Field(...,description="My email")

    phone : str = Field(..., description="My phone number")

    GEMINI_API_KEY: str = Field(...,description="API Key")
    
    NEO4J_URL: str = Field(..., description="URL for the neo4j aura DB")
    
    NEO4J_USERNAME: str = Field(..., description="Username for the neo4j credentials")
    
    NEO4J_PASSWORD: str = Field(...,description="Password for neo4j")
    
    NEO4J_DATABASE: str = Field(...,description="Name of neo4j database")
    
    NEO4J_TRANSPORT: str = Field(...,description="Transport type, http, sse, stdio")
    
    NEO4J_MCP_SERVER_HOST: str = Field(..., description="Host address of MCP server for neo4j")
    
    NEO4J_MCP_SERVER_PORT: int = Field(..., description="Port for neo4j MCP server")
    
    NEO4J_MCP_SERVER_PATH: str = Field(..., description="Path of MCP server")

    model_config = SettingsConfigDict(env_file='.env',env_file_encoding="utf-8")

Settings = ConfigSettings()