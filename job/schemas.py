from pydantic import BaseModel


class JobBase(BaseModel):
    title: str
    description: str
    salary: float
    job_type: str
    description: str | None = None


class JobCreate(JobBase):
    pass

    class Config:
        from_attributes = True


