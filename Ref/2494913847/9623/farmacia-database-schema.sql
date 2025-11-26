-- Farmácia de Manipulação - Schema PostgreSQL
-- Versão: 1.0.0
-- Data: 2024

-- Criar database
CREATE DATABASE IF NOT EXISTS farmacia_db
    WITH 
    OWNER = farmacia_user
    ENCODING = 'UTF8'
    LC_COLLATE = 'pt_BR.UTF-8'
    LC_CTYPE = 'pt_BR.UTF-8'
    TABLESPACE = pg_default
    CONNECTION LIMIT = -1;

-- Conectar ao database
\c farmacia_db;

-- Criar schema
CREATE SCHEMA IF NOT EXISTS public;

-- Extensões necessárias
CREATE EXTENSION IF NOT EXISTS "uuid-ossp";
CREATE EXTENSION IF NOT EXISTS "pgcrypto";

-- Tabela de clientes
CREATE TABLE IF NOT EXISTS clientes (
    id SERIAL PRIMARY KEY,
    uuid UUID DEFAULT uuid_generate_v4() UNIQUE NOT NULL,
    name VARCHAR(255) NOT NULL,
    email VARCHAR(255),
    phone VARCHAR(20),
    cpf VARCHAR(14),
    birth_date DATE,
    address TEXT,
    city VARCHAR(100),
    state VARCHAR(2),
    zip_code VARCHAR(10),
    notes TEXT,
    tags TEXT[],
    active BOOLEAN DEFAULT true,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    CONSTRAINT unique_email UNIQUE (email),
    CONSTRAINT unique_phone UNIQUE (phone),
    CONSTRAINT unique_cpf UNIQUE (cpf)
);

-- Índices para clientes
CREATE INDEX idx_clientes_email ON clientes(email);
CREATE INDEX idx_clientes_phone ON clientes(phone);
CREATE INDEX idx_clientes_cpf ON clientes(cpf);
CREATE INDEX idx_clientes_active ON clientes(active);

-- Tabela de receitas/pedidos
CREATE TABLE IF NOT EXISTS receitas (
    id SERIAL PRIMARY KEY,
    order_id VARCHAR(50) UNIQUE NOT NULL,
    client_id INTEGER REFERENCES clientes(id),
    client_name VARCHAR(255),
    client_phone VARCHAR(20),
    client_email VARCHAR(255),
    channel VARCHAR(20) NOT NULL CHECK (channel IN ('whatsapp', 'email', 'web', 'phone', 'presencial')),
    status VARCHAR(30) NOT NULL DEFAULT 'received',
    message_content TEXT,
    extracted_text TEXT,
    medication_count INTEGER DEFAULT 0,
    total_amount DECIMAL(10,2),
    budget_data JSONB,
    doctor_name VARCHAR(255),
    doctor_crm VARCHAR(50),
    prescription_date DATE,
    files_stored TEXT[],
    payment_method VARCHAR(30),
    delivery_method VARCHAR(30),
    notes TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    processed_at TIMESTAMP WITH TIME ZONE,
    approved_at TIMESTAMP WITH TIME ZONE,
    cancelled_at TIMESTAMP WITH TIME ZONE,
    completed_at TIMESTAMP WITH TIME ZONE,
    negotiation_requested_at TIMESTAMP WITH TIME ZONE,
    expires_at TIMESTAMP WITH TIME ZONE,
    cancel_reason TEXT,
    metadata JSONB,
    CONSTRAINT valid_status CHECK (status IN (
        'received', 'processing', 'medications_extracted', 'extraction_failed',
        'budget_ready', 'approved', 'negotiating', 'cancelled', 'expired',
        'in_production', 'ready', 'delivered', 'completed'
    ))
);

-- Índices para receitas
CREATE INDEX idx_receitas_order_id ON receitas(order_id);
CREATE INDEX idx_receitas_client_id ON receitas(client_id);
CREATE INDEX idx_receitas_status ON receitas(status);
CREATE INDEX idx_receitas_channel ON receitas(channel);
CREATE INDEX idx_receitas_created_at ON receitas(created_at DESC);
CREATE INDEX idx_receitas_expires_at ON receitas(expires_at);
CREATE INDEX idx_receitas_budget_data ON receitas USING GIN (budget_data);

-- Tabela de medicamentos
CREATE TABLE IF NOT EXISTS medicamentos (
    id SERIAL PRIMARY KEY,
    code VARCHAR(50) UNIQUE,
    name VARCHAR(255) NOT NULL,
    active_ingredient VARCHAR(255),
    category VARCHAR(100),
    unit VARCHAR(20) DEFAULT 'unidade',
    unit_price DECIMAL(10,2) NOT NULL,
    cost_price DECIMAL(10,2),
    tax_rate DECIMAL(4,3) DEFAULT 0.18,
    profit_margin DECIMAL(4,3) DEFAULT 0.35,
    min_stock INTEGER DEFAULT 0,
    current_stock INTEGER DEFAULT 0,
    supplier VARCHAR(255),
    requires_prescription BOOLEAN DEFAULT true,
    controlled BOOLEAN DEFAULT false,
    notes TEXT,
    active BOOLEAN DEFAULT true,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Índices para medicamentos
CREATE INDEX idx_medicamentos_name ON medicamentos(LOWER(name));
CREATE INDEX idx_medicamentos_active ON medicamentos(active);
CREATE INDEX idx_medicamentos_category ON medicamentos(category);
CREATE INDEX idx_medicamentos_controlled ON medicamentos(controlled);

-- Tabela de preços históricos
CREATE TABLE IF NOT EXISTS precos_historico (
    id SERIAL PRIMARY KEY,
    medicamento_id INTEGER REFERENCES medicamentos(id),
    unit_price DECIMAL(10,2) NOT NULL,
    cost_price DECIMAL(10,2),
    valid_from DATE NOT NULL,
    valid_until DATE,
    reason VARCHAR(255),
    created_by VARCHAR(100),
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Índices para preços histórico
CREATE INDEX idx_precos_medicamento ON precos_historico(medicamento_id);
CREATE INDEX idx_precos_validity ON precos_historico(valid_from, valid_until);

-- Tabela de itens do pedido
CREATE TABLE IF NOT EXISTS receita_items (
    id SERIAL PRIMARY KEY,
    receita_id INTEGER REFERENCES receitas(id) ON DELETE CASCADE,
    medicamento_id INTEGER REFERENCES medicamentos(id),
    medication_name VARCHAR(255) NOT NULL,
    dosage VARCHAR(100),
    quantity INTEGER NOT NULL DEFAULT 1,
    unit_price DECIMAL(10,2),
    subtotal DECIMAL(10,2),
    tax_amount DECIMAL(10,2),
    profit_amount DECIMAL(10,2),
    total_amount DECIMAL(10,2),
    instructions TEXT,
    status VARCHAR(30) DEFAULT 'pending',
    produced_at TIMESTAMP WITH TIME ZONE,
    produced_by VARCHAR(100),
    notes TEXT,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Índices para itens
CREATE INDEX idx_items_receita ON receita_items(receita_id);
CREATE INDEX idx_items_medicamento ON receita_items(medicamento_id);
CREATE INDEX idx_items_status ON receita_items(status);

-- Tabela de arquivos
CREATE TABLE IF NOT EXISTS arquivos (
    id SERIAL PRIMARY KEY,
    uuid UUID DEFAULT uuid_generate_v4() UNIQUE NOT NULL,
    receita_id INTEGER REFERENCES receitas(id) ON DELETE CASCADE,
    filename VARCHAR(255) NOT NULL,
    original_name VARCHAR(255),
    mime_type VARCHAR(100),
    size_bytes INTEGER,
    storage_path TEXT,
    storage_type VARCHAR(20) DEFAULT 'local',
    checksum VARCHAR(64),
    ocr_processed BOOLEAN DEFAULT false,
    ocr_result TEXT,
    metadata JSONB,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Índices para arquivos
CREATE INDEX idx_arquivos_receita ON arquivos(receita_id);
CREATE INDEX idx_arquivos_uuid ON arquivos(uuid);
CREATE INDEX idx_arquivos_created ON arquivos(created_at DESC);

-- Tabela de logs de auditoria
CREATE TABLE IF NOT EXISTS audit_logs (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    action VARCHAR(50) NOT NULL,
    entity_type VARCHAR(50),
    entity_id VARCHAR(100),
    order_id VARCHAR(50),
    client_name VARCHAR(255),
    user_id VARCHAR(100),
    source VARCHAR(20),
    ip_address INET,
    user_agent TEXT,
    changes JSONB,
    metadata JSONB,
    success BOOLEAN DEFAULT true,
    error_message TEXT
);

-- Índices para audit logs
CREATE INDEX idx_audit_timestamp ON audit_logs(timestamp DESC);
CREATE INDEX idx_audit_action ON audit_logs(action);
CREATE INDEX idx_audit_order ON audit_logs(order_id);
CREATE INDEX idx_audit_entity ON audit_logs(entity_type, entity_id);

-- Tabela de logs de relatórios
CREATE TABLE IF NOT EXISTS report_logs (
    id SERIAL PRIMARY KEY,
    report_type VARCHAR(50) NOT NULL,
    generated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    period_start DATE,
    period_end DATE,
    data JSONB,
    sent_email BOOLEAN DEFAULT false,
    sent_slack BOOLEAN DEFAULT false,
    recipients TEXT[],
    status VARCHAR(20) DEFAULT 'generated',
    error TEXT
);

-- Índices para report logs
CREATE INDEX idx_reports_type ON report_logs(report_type);
CREATE INDEX idx_reports_generated ON report_logs(generated_at DESC);

-- Tabela de logs de monitoramento
CREATE TABLE IF NOT EXISTS monitoring_logs (
    id SERIAL PRIMARY KEY,
    timestamp TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    check_type VARCHAR(50) NOT NULL,
    service VARCHAR(50),
    status VARCHAR(20),
    response_time_ms INTEGER,
    details JSONB,
    alerted BOOLEAN DEFAULT false,
    alert_sent_at TIMESTAMP WITH TIME ZONE,
    resolved_at TIMESTAMP WITH TIME ZONE
);

-- Índices para monitoring logs
CREATE INDEX idx_monitoring_timestamp ON monitoring_logs(timestamp DESC);
CREATE INDEX idx_monitoring_type ON monitoring_logs(check_type);
CREATE INDEX idx_monitoring_status ON monitoring_logs(status);

-- Tabela de sessões/tokens
CREATE TABLE IF NOT EXISTS sessions (
    id SERIAL PRIMARY KEY,
    token VARCHAR(255) UNIQUE NOT NULL,
    client_id INTEGER REFERENCES clientes(id),
    order_id VARCHAR(50),
    data JSONB,
    expires_at TIMESTAMP WITH TIME ZONE NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    last_activity TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP
);

-- Índices para sessions
CREATE INDEX idx_sessions_token ON sessions(token);
CREATE INDEX idx_sessions_expires ON sessions(expires_at);

-- Tabela de configurações
CREATE TABLE IF NOT EXISTS configuracoes (
    id SERIAL PRIMARY KEY,
    key VARCHAR(100) UNIQUE NOT NULL,
    value TEXT,
    type VARCHAR(20) DEFAULT 'string',
    category VARCHAR(50),
    description TEXT,
    editable BOOLEAN DEFAULT true,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT CURRENT_TIMESTAMP,
    updated_by VARCHAR(100)
);

-- Configurações padrão
INSERT INTO configuracoes (key, value, type, category, description) VALUES
('tax_rate_default', '0.18', 'decimal', 'finance', 'Taxa de imposto padrão'),
('profit_margin_default', '0.35', 'decimal', 'finance', 'Margem de lucro padrão'),
('delivery_fee_default', '10.00', 'decimal', 'finance', 'Taxa de entrega padrão'),
('discount_threshold', '3', 'integer', 'finance', 'Quantidade mínima para desconto'),
('discount_percentage', '0.05', 'decimal', 'finance', 'Percentual de desconto'),
('budget_expiry_hours', '48', 'integer', 'business', 'Horas para expiração do orçamento'),
('production_time_days', '2', 'integer', 'business', 'Prazo padrão de produção em dias'),
('whatsapp_rate_limit', '1000', 'integer', 'integration', 'Limite diário de mensagens WhatsApp'),
('email_check_interval', '60', 'integer', 'integration', 'Intervalo de verificação de email em segundos'),
('ocr_timeout', '30000', 'integer', 'integration', 'Timeout para OCR em milissegundos'),
('max_file_size', '10485760', 'integer', 'system', 'Tamanho máximo de arquivo em bytes (10MB)'),
('allowed_extensions', '.jpg,.jpeg,.png,.pdf,.bmp', 'string', 'system', 'Extensões de arquivo permitidas'),
('business_hours_start', '08:00', 'string', 'business', 'Horário de abertura'),
('business_hours_end', '18:00', 'string', 'business', 'Horário de fechamento'),
('working_days', 'mon,tue,wed,thu,fri', 'string', 'business', 'Dias úteis')
ON CONFLICT (key) DO NOTHING;

-- Views úteis

-- View de pedidos com informações completas
CREATE OR REPLACE VIEW v_pedidos_completos AS
SELECT 
    r.*,
    c.name as cliente_nome_completo,
    c.cpf as cliente_cpf,
    COUNT(DISTINCT ri.id) as total_itens,
    SUM(ri.quantity) as total_unidades,
    STRING_AGG(DISTINCT ri.medication_name, ', ') as medicamentos_lista
FROM receitas r
LEFT JOIN clientes c ON r.client_id = c.id
LEFT JOIN receita_items ri ON r.id = ri.receita_id
GROUP BY r.id, c.id;

-- View de estatísticas diárias
CREATE OR REPLACE VIEW v_estatisticas_diarias AS
SELECT 
    DATE(created_at) as data,
    COUNT(*) as total_pedidos,
    COUNT(CASE WHEN status = 'approved' THEN 1 END) as pedidos_aprovados,
    COUNT(CASE WHEN status = 'cancelled' THEN 1 END) as pedidos_cancelados,
    SUM(CASE WHEN status = 'approved' THEN total_amount ELSE 0 END) as faturamento,
    COUNT(DISTINCT client_email) as clientes_unicos,
    COUNT(DISTINCT channel) as canais_utilizados
FROM receitas
GROUP BY DATE(created_at);

-- View de medicamentos mais vendidos
CREATE OR REPLACE VIEW v_top_medicamentos AS
SELECT 
    m.id,
    m.name,
    m.category,
    COUNT(DISTINCT ri.receita_id) as numero_pedidos,
    SUM(ri.quantity) as quantidade_total,
    SUM(ri.total_amount) as receita_total,
    AVG(ri.unit_price) as preco_medio
FROM medicamentos m
JOIN receita_items ri ON m.id = ri.medicamento_id
JOIN receitas r ON ri.receita_id = r.id
WHERE r.status IN ('approved', 'in_production', 'ready', 'delivered', 'completed')
GROUP BY m.id;

-- Funções úteis

-- Função para calcular idade
CREATE OR REPLACE FUNCTION calculate_age(birth_date DATE)
RETURNS INTEGER AS $$
BEGIN
    RETURN DATE_PART('year', AGE(birth_date));
END;
$$ LANGUAGE plpgsql;

-- Função para atualizar updated_at automaticamente
CREATE OR REPLACE FUNCTION update_updated_at_column()
RETURNS TRIGGER AS $$
BEGIN
    NEW.updated_at = CURRENT_TIMESTAMP;
    RETURN NEW;
END;
$$ LANGUAGE plpgsql;

-- Triggers para updated_at
CREATE TRIGGER update_clientes_updated_at BEFORE UPDATE ON clientes
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_medicamentos_updated_at BEFORE UPDATE ON medicamentos
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

CREATE TRIGGER update_configuracoes_updated_at BEFORE UPDATE ON configuracoes
    FOR EACH ROW EXECUTE FUNCTION update_updated_at_column();

-- Função para limpar dados antigos
CREATE OR REPLACE FUNCTION cleanup_old_data()
RETURNS void AS $$
BEGIN
    -- Remove logs de auditoria com mais de 2 anos
    DELETE FROM audit_logs WHERE timestamp < CURRENT_TIMESTAMP - INTERVAL '2 years';
    
    -- Remove logs de monitoramento com mais de 90 dias
    DELETE FROM monitoring_logs WHERE timestamp < CURRENT_TIMESTAMP - INTERVAL '90 days';
    
    -- Remove sessões expiradas há mais de 30 dias
    DELETE FROM sessions WHERE expires_at < CURRENT_TIMESTAMP - INTERVAL '30 days';
    
    -- Remove pedidos cancelados há mais de 1 ano
    DELETE FROM receitas WHERE status = 'cancelled' AND cancelled_at < CURRENT_TIMESTAMP - INTERVAL '1 year';
END;
$$ LANGUAGE plpgsql;

-- Índices adicionais para performance
CREATE INDEX idx_receitas_composite ON receitas(status, created_at DESC);
CREATE INDEX idx_items_composite ON receita_items(receita_id, status);
CREATE INDEX idx_audit_composite ON audit_logs(order_id, timestamp DESC);

-- Permissões
GRANT ALL PRIVILEGES ON ALL TABLES IN SCHEMA public TO farmacia_user;
GRANT ALL PRIVILEGES ON ALL SEQUENCES IN SCHEMA public TO farmacia_user;
GRANT ALL PRIVILEGES ON ALL FUNCTIONS IN SCHEMA public TO farmacia_user;

-- Comentários nas tabelas
COMMENT ON TABLE clientes IS 'Tabela de clientes da farmácia';
COMMENT ON TABLE receitas IS 'Tabela principal de receitas/pedidos';
COMMENT ON TABLE medicamentos IS 'Catálogo de medicamentos disponíveis';
COMMENT ON TABLE receita_items IS 'Itens individuais de cada receita';
COMMENT ON TABLE arquivos IS 'Arquivos anexados às receitas';
COMMENT ON TABLE audit_logs IS 'Log de auditoria de todas as ações';
COMMENT ON TABLE monitoring_logs IS 'Logs de monitoramento do sistema';
COMMENT ON TABLE configuracoes IS 'Configurações globais do sistema';