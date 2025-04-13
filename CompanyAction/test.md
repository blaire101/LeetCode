flowchart TD
    subgraph Ingestion
        A[User Upload API] --> C[Cloud Storage 7 day retention]
        B[Kafka Producer] --> C
    end

    C --> D[Trigger: on finalize event --> Cloud Run / Cloud Functions]

    D --> E[Image Processing]
    E --> E1[1. Write processed image --> Cloud Storage 7 day]
    E --> E2[2. Write structured metadata --> BigQuery]

    E2 --> F[BI Tools e.g. Data Studio connect to BigQuery]
